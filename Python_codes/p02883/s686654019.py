def isok(x):
    res=0
    for i in range(n):
        res+=max(a[i]-x//f[i],0)
        if res>k:
            return False
    if res>k:
        return False
    else:
        return True

n,k=map(int,input().split())
a=sorted(map(int,input().split()))
f=sorted(map(int,input().split()),reverse=True)

ng,ok=-1,10**18
while(ok-ng>1):
    mid=(ok+ng)//2
    if isok(mid):
        ok=mid
    else:
        ng=mid
print(ok)