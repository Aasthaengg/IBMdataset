import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')
    
    
x,t=map(int,input().split())
print(max((x-t),0))