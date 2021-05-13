H,W,N = map(int,input().split())
ab = [list(map(int,input().split())) for _ in [0]*N]

d = {}
for a,b in ab:
    for da in (-1,0,1):
        for db in (-1,0,1):
            if not ( 2<=a+da<=H-1 and 2<=b+db<=W-1):continue
            d[(a+da,b+db)] = d.get((a+da,b+db),0)+1

ans = [0]*10
for v in d.values():
    ans[v] += 1
ans[0] = (H-2)*(W-2) - sum(ans[1:])
print(*ans,sep="\n")