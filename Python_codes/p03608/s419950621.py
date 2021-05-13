N,M,r = map(int,input().split())
R = list(map(int,input().split()))
#dp[i][j][k] -> 町iまで経由地点として使える。j,kの最短移動距離
dp = [[float("INF")]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    dp[a][b] = c
    dp[b][a] = c

for i in range(N+1):
    dp[i][i] = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(N+1):
            dp[j][k] = min(dp[j][k],dp[j][i]+dp[i][k])

from itertools import permutations
ans = float("INF")
for pattern in permutations(R):
    cost = 0
    for i in range(r-1):
        cost += dp[pattern[i]][pattern[i+1]]
    ans = min(ans,cost)
print(ans)