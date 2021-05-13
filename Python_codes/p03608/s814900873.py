from itertools import permutations
N,M,R = map(int,input().split())
RList = list(map(int,input().split()))
dp = [[float("INF")]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][i] = 0
for _ in range(M):
    a,b,c = map(int,input().split())
    dp[a][b] = c
    dp[b][a] = c

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            dp[j][k] = min(dp[j][i]+dp[i][k],dp[j][k])

ans = float("INF")
RList = list(permutations(RList))
for Rs in RList:
    tmp = 0
    for i in range(1,R):
        a = Rs[i-1]
        b = Rs[i]
        tmp += dp[a][b]
    ans = min(ans,tmp)
print(ans)