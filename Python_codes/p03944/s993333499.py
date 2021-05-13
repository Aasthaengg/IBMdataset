W,H,N=map(int,input().split())
xya=[list(map(int,input().split()))for _ in range(N)]

wl=0
wr=W
hd=0
hu=H
for x,y,a in xya:
    if a==1:
        wl=max(wl,x)
    elif a==2:
        wr=min(wr,x)
    elif a==3:
        hd=max(hd,y)
    else:
        hu=min(hu,y)

ans=max(wr-wl,0)*max(hu-hd,0)
print(ans)