import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')
    
    
n=int(input())
a=int(input())

print(n**2-a)