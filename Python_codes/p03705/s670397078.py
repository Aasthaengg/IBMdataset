import sys
input=sys.stdin.buffer.readline
n,a,b=map(int,input().split())
if n==1:
    if a==b:print(1)
    if a!=b:print(0)
if n>1:
    if a>b:print(0)
    if a<=b:print((n-2)*(b-a)+1)