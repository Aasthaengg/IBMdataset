import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')
    
    
a,b,c=map(int,input().split())

if c-b==b-a:
	print("YES")
else:
	print("NO")
