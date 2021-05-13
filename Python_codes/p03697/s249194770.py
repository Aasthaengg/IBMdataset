import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')
    
    
a,b=map(int,input().split())

if a+b>=10:print("error")
else:print(a+b)