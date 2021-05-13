H,W,N=map(int,input().split())
ab=[list(map(int,input().split())) for _ in [0]*N]
d={}
for a,b in ab:
    for i in (a-1,a,a+1):
        for j in (b-1,b,b+1):
            d[(i,j)] = d.get((i,j),0)+1
cnt = [0]*10
for k,v in d.items():
    a,b = k
    if a<2 or b<2:continue
    if a>H-1 or b>W-1:continue
    cnt[v] += 1
cnt[0] = (W-2)*(H-2)-sum(cnt)
for ans in cnt:
    print(ans)
