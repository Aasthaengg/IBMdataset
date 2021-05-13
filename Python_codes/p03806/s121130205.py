N, Ma, Mb = map(int, input().split())
a = [0]*N
b = [0]*N
c = [0]*N
INF = 10000


for i in range(N):
    a[i], b[i], c[i] = map(int, input().split())

#dp[i][j][k]...i番目までの品物で, タイプAの物質をjグラム, タイプBの物質をkグラム調達するのに必要な費用の最小値

dp = [[[INF]*400 for _ in range(400)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(1, N+1):
    for j in range(400):
        for k in range(400):
            if j < a[i-1] or k < b[i-1]:
                dp[i][j][k] = dp[i-1][j][k]
            else:
                dp[i][j][k] = min(dp[i-1][j][k], dp[i-1][j-a[i-1]][k-b[i-1]]+c[i-1])

ans = INF

for i in range(1, N+1):
    for j in range(1, 400):
        for k in range(1, 400):
            if j*Mb == k*Ma:
                ans = min(ans, dp[i][j][k])
if ans == INF:
    print(-1)
else:
    print(ans)


