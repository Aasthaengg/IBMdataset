import sys
m,b=map(int,sys.stdin.readline().split())
if b%m==0:
    print(m+b)
else:
    print(b-m)