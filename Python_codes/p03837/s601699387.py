N,M = map(int, input().split())
INF = 10**6
Edge = [[INF]*N for _ in range(N)]
for _ in range(M):
    a,b,c = map(int, input().split())
    Edge[a-1][b-1] = c
    Edge[b-1][a-1] = c
    
dp = [[INF]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            dp[i][j] = 0
        else:
            dp[i][j] = Edge[i][j]
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        if Edge[i][j] == INF:
            continue
        if Edge[i][j] > dp[i][j]:
            ans += 1
            
print(ans)