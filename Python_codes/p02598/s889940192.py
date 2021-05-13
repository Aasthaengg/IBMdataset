n,k=list(map(int,input().split()))
alst=list(map(lambda x:int(x)*100,input().split()))

ok=max(alst)
ng=0

while abs(ok-ng)>1:
    cen=(ok+ng)//2

    cnt=0

    for a in alst:
        cnt+=(a+cen-1)//cen-1

    if cnt<=k:
        ok=cen
    else:
        ng=cen+1

if ok%100==0:
    print(ok//100)
else:
    print(ok//100+1)