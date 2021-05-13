import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')
    
    
r=int(input())
g=int(input())

print(g+g-r)