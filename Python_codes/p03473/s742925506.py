import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')
    
    
print(48-int(input()))