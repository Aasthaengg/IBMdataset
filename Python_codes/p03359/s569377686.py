import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')
    
a,b=map(int,input().split())

if b<a:
	print(a-1)
else:
	print(a)