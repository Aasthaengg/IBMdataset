N=int(input())

def is_ok(n):
    if n*(n+1)//2>=N:
        return True
    else:
        return False

ng=0
ok=N+1

while abs(ng-ok)>1:
    mid=(ok+ng)//2

    if is_ok(mid):
        ok=mid
    else:
        ng=mid

diff=ok*(ok+1)//2-N

for i in range(1,ok+1):
    if i!=diff:
        print(i)