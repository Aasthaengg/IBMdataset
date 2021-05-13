h,w,m=map(int,input().split())

cx=[0]*w
cy=[0]*h
xy=set()
for _ in range(m):
    y,x=map(int,input().split())
    x,y=x-1,y-1
    cx[x]+=1
    cy[y]+=1
    xy.add((x,y))

xmx=max(cx)
ymx=max(cy)
xs=[x for x in range(w) if cx[x]==xmx]
ys=[y for y in range(h) if cy[y]==ymx]

ans=xmx+ymx-1
ok=False
for y in ys:
    for x in xs:
        if (x,y) not in xy:
            ans+=1
            ok=True
            break
    if ok:
        break

print(ans)
