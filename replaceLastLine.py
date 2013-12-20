#coding=utf8
import linecache
import os

def replaceLastLine(filename,linano):
	f = open(filename,"rb")

	current_line = 1
	while current_line < linano:
		f.readline()
		current_line += 1

	seekpoint = f.tell()
	fw = open(filename,"r+b")
	fw.seek(seekpoint,0)

	print f.readline()

	chars = f.readline()
	while chars:
		fw.writelines(chars)
		chars = f.readline()

	f.close()
	fw.truncate()
	fw.close()

def readLine(filename,linano):
	count = linecache.getline(filename,linano)
	print count

def getFileLines(filename):
	count = -1
	for count,line in enumerate(open(filename,'rU')):
		pass
	count += 1
	print count
	return count

def go(dir):
	for lists in os.listdir(dir):
		path = os.path.join(dir,lists)
		
		if os.path.isdir(path):
			go(path)
		else:
			print path
			replaceLastLine(path,getFileLines(path))
			#readLine(path,getFileLines(path))

def main():
	root = raw_input('input root dir: ')
	go(root)

main()