import sys
input=sys.stdin.readline
n,k=map(int,input().split())
l=list(map(int,input().split()))
ok=max(l)
ng=0
def solve(m):
    s=0
    for i in l:
        s+=-((-i)//m)-1
    return s

while ok-ng>1:
    m=(ok+ng)//2
    if k<solve(m):
        ng=m
    else:
        ok=m
print(ok)