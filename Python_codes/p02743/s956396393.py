import sys,math,collections,itertools
input = sys.stdin.readline

a,b,c=list(map(int,input().split()))

if c-a-b <0:
    print('No')
    exit()

if (c-a-b)**2 > 4*a*b:
    print('Yes')
else:
    print('No')
