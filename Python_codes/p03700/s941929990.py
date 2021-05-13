n,a,b=map(int,input().split())
h=[int(input()) for _ in range(n)]
c=a-b

ok=10**9
ng=0

while ok-ng>1:
    cen=(ok+ng)//2
    cnt=0

    for hh in h:
        hh-=b*cen

        cnt+=max(0,(hh+c-1)//c)
    
    if cnt<=cen:
        ok=cen
    else:
        ng=cen

print(ok)