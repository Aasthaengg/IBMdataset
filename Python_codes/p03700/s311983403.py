N,A,B=map(int,input().split())

H=[]
for _ in range(N):
    H.append(int(input()))

ok=10**9+1
ng=0

while ok-ng>1:
    mid=(ok+ng)//2
    dmg=B*mid
    tgt=0
    for item in H:
        tgt+=-(-max(item-dmg,0)//(A-B))
    if tgt<=mid:
        ok=mid
    else:
        ng=mid

print(ok)