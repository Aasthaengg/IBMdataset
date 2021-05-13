h,w,m=map(int,input().split())

xsct=[0]*w
ysct=[0]*h
ips=set()
for _ in range(m):
    y,x=map(int,input().split())
    x,y=x-1,y-1
    xsct[x]+=1
    ysct[y]+=1
    ips.add((x,y))

xsmx=max(xsct)
ysmx=max(ysct)

xs=[x for x in range(w) if xsct[x]==xsmx]
ys=[y for y in range(h) if ysct[y]==ysmx]

ans=xsmx+ysmx-1
ok=False
for y in ys:
    for x in xs:
        if (x,y) not in ips:
            ans+=1
            ok=True
            break
    if ok:
        break

print(ans)
