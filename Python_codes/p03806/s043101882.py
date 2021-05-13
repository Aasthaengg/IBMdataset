inf = float('inf')

N,Ma,Mb = map(int,input().split())
abc = [list(map(int,input().split())) for _ in range(N)]

# dp[i][j][k]: i番目までみてj(g), k(g)となるような最小予算
dp = [[[inf]*401 for _ in range(401)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    a,b,c = abc[i]
    for j in range(401):
        for k in range(401):
            if j - a >= 0 and k - b >= 0:
                dp[i+1][j][k] = min(dp[i][j][k], dp[i][j-a][k-b] + c)
            else:
                dp[i+1][j][k] = dp[i][j][k]

ans = inf

for j in range(1,401):
    for k in range(1,401):
        if j * Mb == Ma * k:
            ans = min(ans, dp[N][j][k])

if ans == inf:
    ans = -1
print(ans)