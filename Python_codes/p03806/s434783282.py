n,ma,mb = map(int,input().split())
l = [list(map(int,input().split())) for i in range(n)]

dp = [[[float("INF")]*(n*10+2) for i in range(n*10+2)] for j in range(n+1)]

dp[0][0][0] = 0

for i in range(n):
    a,b,c = l[i]
    
    for j in range(n*10+1):
        for k in range(n*10+1):
            
            if j >= a and k >= b:
                dp[i+1][j][k] = min(dp[i][j][k],dp[i][j-a][k-b]+c)
            elif dp[i][j][k] != float("INF"):
                dp[i+1][j][k] = dp[i][j][k]
ans = float("INF")

for i in range(1,n*10+1):
    j = i*mb/ma
    if j%1 == 0 and j < n*10:
        ans = min(ans,dp[-1][i][int(j)])
if ans == float("INF"):
    print(-1)
else:
    print(ans)
