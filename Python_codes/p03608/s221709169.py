N,M,R = map(int,input().split())
R = list(map(int,input().split()))
dp = [[float("INF")]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][i] = 0

for _ in range(M):
    a,b,c = map(int,input().split())
    dp[a][b] = min(dp[a][b],c)
    dp[b][a] = min(dp[b][a],c)

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            dp[j][k] = min(dp[j][k],dp[j][i]+dp[i][k])

def dfs(p,n,path,cost):
    path.add(n)
    cost += dp[p][n]
    
    if len(path) == len(R):
        return cost
    else:
        res = float("INF")
        for r in R:
            if r not in path:
                res = min(res,dfs(n,r,path,cost))
                path.remove(r)
        return res
ans = float("INF")
for r in R:
    ans = min(ans,dfs(r,r,set(),0))
print(ans)