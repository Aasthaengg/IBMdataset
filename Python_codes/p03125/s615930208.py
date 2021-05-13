import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')

a,b=map(int,input().split())

if b%a==0:
	print(a+b)
else:
	print(b-a)