N,Ma,Mb = map(int,input().split())

INF = 10000

dp = [[[INF for b in range(401)] for a in range(401)] for i in range(N+1)]

dp[0][0][0] = 0

for i in range(1,N+1):
    ai,bi,ci = map(int,input().split())
    for a in range(401):
        for b in range(401):
            if a-ai >= 0 and b-bi >= 0:
                dp[i][a][b] = min(dp[i-1][a][b],dp[i-1][a-ai][b-bi]+ci)
            else:
                dp[i][a][b] = dp[i-1][a][b]

ans = INF
for j in range(1,401):
    if Ma*j >= 400 or Mb*j >= 400:
        break
    ans = min(ans,dp[N][Ma*j][Mb*j])
print(ans if ans != INF else -1)

