import sys
input=sys.stdin.buffer.readline
a,b,c,k=map(int,input().split())
if k % 2 ==0:
    print(a-b)
else:print(-a+b)