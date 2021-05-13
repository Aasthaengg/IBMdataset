import sys
input=sys.stdin.readline

n,a,b=map(int,input().split())
x=a-b
h=[int(input()) for _ in range(n)]
ok=10**9+1
ng=0
while ok-ng>1:
    m=(ok+ng)//2
    k=0
    for i in range(n):
        k+=(max(0,h[i]-m*b)+x-1)//x
    if k<=m:
        ok=m
    else:
        ng=m
print(ok)
