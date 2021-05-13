import sys

n,a,b = map(int,input().split())

if n == 1:
    if a != b:
        print(0)
        exit()

if a > b:
    print(0)
    exit()
    
print(-(a*(n-1)+b)+(a+b*(n-1))+1)