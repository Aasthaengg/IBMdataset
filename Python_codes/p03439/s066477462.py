n=int(input())

def q(i):
    print(i)
    r=input()
    if r=='Vacant':exit()
    return r

t=q(0)

def is_ok(x):
    s=q(x)
    if x%2:
        return t!=s
    else:
        return t==s

ok=0
ng=n

while ng-ok:
    mid=(ok+ng)//2
    if is_ok(mid):
        ok=mid
    else:
        ng=mid