from math import ceil
def isok(x):
    res=0
    for i in range(N):
        H=h[i]-B*x
        if H<=0:
            continue
        res+=ceil(H/(A-B))
    return True if res<=x else False

N,A,B=map(int,input().split())
h=[int(input()) for i in range(N)]

ng,ok=-1,10**10
while(ok-ng>1):
    mid=(ok+ng)//2
    if isok(mid):
        ok=mid
    else:
        ng=mid
print(ok)