n,k = list(map(int,input().split()))
a = list(map(int,input().split()))

ng=0
ok=max(a)+1

while ok-ng>1:
    mid = (ok+ng)//2
    cur=0
    for x in a:
        cur+=(x-1)//mid
    if cur>k:
        ng=mid
    else:
        ok=mid
print(ok)
