N, K = map(int, input().split())
Np1 = N+1
ans = 0
for b in range(1, Np1):
    r = b - K
    if r <= 0:
        continue
    for a in range(max(1,K), Np1, b):
        ans += min(a+r, Np1) - a
print(ans)