h, n = map(int, input().split())
a = []
b = []
for _ in range(n):
    tmp_a, tmp_b = map(int, input().split())
    a.append(tmp_a)
    b.append(tmp_b)

dp = [[float('inf')] * (h+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(h+1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        dp[i+1][min(j+a[i], h)] = min(dp[i+1][min(j+a[i], h)], dp[i+1][j] + b[i])

print(dp[n][h])