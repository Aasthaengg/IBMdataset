N,Ma,Mb = map(int,input().split())
abc = [ list(map(int,input().split())) for i in range(N)]

dp = [ [ [ float("inf") for i in range(401)] for j in range(401)] for k in range(N+1)]
dp[0][0][0] = 0
for i in range(N):
    for j in range(401):
        for k in range(401):
            if j - abc[i][0] >= 0 and k - abc[i][1] >= 0:
                dp[i+1][j][k] = min(dp[i][j][k],dp[i][j-abc[i][0]][k-abc[i][1]] + abc[i][2])

            else:
                dp[i+1][j][k] = dp[i][j][k]


ans = float("inf")
for i in range(1,401):
    for j in range(1,401):
        if (i / j ) == (Ma / Mb):
            ans = min(ans , dp[N][i][j])

if ans == float("inf"):
    print(-1)
else:
    print(ans)
