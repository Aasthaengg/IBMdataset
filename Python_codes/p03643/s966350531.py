import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')
    

S=input()

print("ABC"+S)