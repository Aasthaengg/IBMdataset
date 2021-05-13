INF = 10**10

n,ma,mb = map(int, input().split())
dp = [[[INF] * 500 for i in range(500)] for i in range(n+1)]
dp[0][0][0] = 0
for i in range(n):
    a,b,c = map(int, input().split())
    for w_a in range(500):
        for w_b in range(500):
            dp[i+1][w_a][w_b] = dp[i][w_a][w_b]
    for w_a in range(500):
        for w_b in range(500):
            if dp[i][w_a][w_b] == INF : continue
            dp[i+1][w_a+a][w_b+b] = min(dp[i][w_a+a][w_b+b], dp[i][w_a][w_b]+c)

a = 0
b = 0
dp[n][0][0] = INF
# ma.mbは互いに素
ans = INF
while a < 500 and b < 500:
    ans = min(ans,dp[n][a][b])
    a += ma
    b += mb
if ans == INF:
    print(-1)
else:print(ans)