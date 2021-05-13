# 安いお店から買えるだけ買う
n,m = list(map(int, input().split()))
ab = sorted([tuple(map(int, input().split())) for _ in range(n)])

ans = 0
for a,b in ab:
    c = min(m,b)
    ans+=a*c
    m-=c
    if m==0:
        break

print(ans)