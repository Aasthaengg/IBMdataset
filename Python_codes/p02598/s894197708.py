f=lambda:map(int,input().split())
N,K=f()
A=list(f())

def isOK(X):
    if X<=0:
        return False
    return sum([-a//X*-1-1 for a in A])<=K


ok=10**10
ng=-1
while abs(ok-ng)>1:
    mid=(ok+ng)//2
    if isOK(mid):
        ok=mid
    else:
        ng=mid
print(ok)