N,T = map(int,input().split())
ts = list(map(int,input().split()))

ans = 0
prev = ts[0]
for t in ts[1:]:
    ans += min(T, t-prev)
    prev = t
ans += T
print(ans)