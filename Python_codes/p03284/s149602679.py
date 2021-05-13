import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')

n,k=map(int,input().split())

if (n%k)==0:
	print(0)
else:
	print(1)