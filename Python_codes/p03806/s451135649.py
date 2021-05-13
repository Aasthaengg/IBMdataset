

N, Ma, Mb = map(int, input().split())

a = [0] * N
b = [0] * N
c = [0] * N
for i in range(N):
    a[i], b[i], c[i] = map(int, input().split())
    

INF = float("inf")
sA = sum(a)
sB = sum(b)
# 薬A,Bの合計がi,jになるのに必要な最小金額
dp = [[[INF for _ in range(401)] for _ in range(401)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    for j in range(401):
        for k in range(401):
            if a[i] <= j and  b[i] <= k:
                dp[i+1][j][k] = min(dp[i][j][k], dp[i][j - a[i]][k - b[i]] + c[i])
            else:
                dp[i+1][j][k] = dp[i][j][k]


ans = INF

x = Ma
y = Mb
while x <= sA and y <= sB :

    ans = min(ans, dp[N][x][y])
    x += Ma
    y += Mb


if ans == INF:
    ans = -1
print(ans)


