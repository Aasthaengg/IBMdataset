import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

w,h,n=map(int,input().split())
u,d,r,l=h,0,w,0
for _ in range(n):
    x,y,a=map(int,input().split())
    if a==1:
        if l<x: l=x
    elif a==2:
        if r>x: r=x
    elif a==3:
        if d<y: d=y
    elif a==4:
        if u>y: u=y

if r-l<=0 or u-d<=0:
    print(0)
else:
    print((r-l)*(u-d))