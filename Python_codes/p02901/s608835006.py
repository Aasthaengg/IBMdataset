n, m = map(int, input().split())
dp = [float("INF")]*(1<<n)
dp[0] = 0
for _ in range(m):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    C = 0
    for e in c:
        C += 1<<(e-1)
    for i in range(1<<n): 
        dp[i|C] = min(dp[i|C], dp[i]+a)
if dp[-1] == float("INF"): print(-1)
else: print(dp[-1])