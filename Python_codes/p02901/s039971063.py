N, M = map(int, input().split())

INF = float("inf")
dp = [INF for i in range(2**N)]
dp[0] = 0
for i in range(M):
    a, b = map(int, input().split())
    C = list(map(int, input().split()))
    key = 0
    for c in C:
        key += 2**(c-1)
    for j in range(len(dp)-1, -1, -1):
        if dp[j] == INF:
            continue
        if dp[j | key] > dp[j] + a:
            dp[j | key] = dp[j] + a
            
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
