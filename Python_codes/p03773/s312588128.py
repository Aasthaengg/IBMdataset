import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')
   
a,b=map(int,input().split())

print((a+b)%24)