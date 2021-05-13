K=int(input())
A=list(map(int,input().split()))

def func(num):
    for item in A:
        num=num//item*item
    return num

ok=10**20
ng=0

while ok-ng>1:
    mid=(ok+ng)//2
    if func(mid)>=2:
        ok=mid
    else:
        ng=mid

low=ok

ok=10**20
ng=0

while ok-ng>1:
    mid=(ok+ng)//2
    if func(mid)>=4:
        ok=mid
    else:
        ng=mid

high=ng

if func(low)==2 and func(high)==2:
    print(low,high)
else:
    print(-1)
