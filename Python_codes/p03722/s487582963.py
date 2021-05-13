N,M = map(int,input().split())
dp = [-float("INF")]*(N+1)
dp[1] = 0
edges = [list(map(int,input().split())) for _ in range(M)]
cnt = 0
while cnt < N:
    cnt += 1
    for a,b,c in edges:
        dp[b] = max(dp[a]+c,dp[b])
tmp = dp[N]
cnt = 0
while cnt < N:
    cnt += 1
    for a,b,c in edges:
        dp[b] = max(dp[a]+c,dp[b])
if dp[N] > tmp:
    print("inf")
else:
    print(dp[N])