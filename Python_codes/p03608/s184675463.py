N,M,R = map(int,input().split())
R = list(map(int,input().split()))
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
            dp[j][k] = min(dp[j][k],dp[j][i]+dp[i][k])

candidate = []
def dfs (r,cost,path=set()):
    path.add(r)
    if len(path) == len(R):
        candidate.append(cost)
    else:
        for nx in R:
            if nx not in path:
                dfs(nx,cost+dp[r][nx],path)
    path.remove(r)

for r in R:
    dfs(r,0)
print(min(candidate))

