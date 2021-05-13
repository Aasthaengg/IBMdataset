ma = lambda :map(int,input().split())
h,w,d = ma()
area_d = [[] for i in range(d)]
rs = [[0] for i in range(d)]
for i in range(h):
    for j,a in enumerate(ma()):
        area_d[a%d].append((a,i,j))
for i in range(d):
    area_d[i].sort()

for i in range(d):
    yp,xp = 0,0
    for a,y,x in area_d[i]:
        rs[i].append(rs[i][-1] + abs(y-yp)+abs(x-xp))
        yp,xp = y,x
q = int(input())
for i in range(q):
    l,r = ma()
    lq,lr = divmod(l,d)
    rq,rr = divmod(r,d)
    if lr==0:print(rs[lr][rq] - rs[lr][lq])
    else:print(rs[lr][rq+1] - rs[lr][lq+1])
