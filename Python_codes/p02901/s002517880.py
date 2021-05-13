N, M = map(int,input().split())
key = [0] * M
cost = [0] * M
for i in range(M):
    a, b = map(int,input().split())
    cost[i] = a
    key_id = list(map(int,input().split()))
    for j in range(b):
        key[i] |= (1 << (key_id[j] - 1))
dp = [[float("inf")] * (1<<N)] * (M + 1)
dp[0][0] = 0
for i in range(M):
    for j in range(1<<N):
        if dp[i + 1][j | key[i]] > dp[i][j] + cost[i]:
            dp[i + 1][j | key[i]] = dp[i][j] + cost[i]
        if dp[i + 1][j] > dp[i][j]:
            dp[i + 1][j] = dp[i][j]
if dp[-1][-1] == float("inf"):
    print(-1)
else:
    print(dp[-1][-1])