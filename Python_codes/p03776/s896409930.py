n, a, b = map(int, input().split())
v = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]
d = [[0] * (n + 1) for _ in range(n + 1)]
d[0][0] = 1
for i in range(n):
    for j in range(i + 1):
        if dp[i + 1][j] < dp[i][j]:
            d[i + 1][j] = d[i][j]
            dp[i + 1][j] = dp[i][j]
        elif dp[i + 1][j] == dp[i][j]:
            d[i + 1][j] += d[i][j]
        if dp[i + 1][j + 1] < dp[i][j] + v[i]:
            d[i + 1][j + 1] = d[i][j]
            dp[i + 1][j + 1] = dp[i][j] + v[i]
        elif dp[i + 1][j + 1] == dp[i][j] + v[i]:
            d[i + 1][j + 1] += d[i][j]
ans = 0
idx = float('inf')
cnt = 0
for i in range(a, b + 1):
    if dp[n][i] * idx > ans * i:
        ans = dp[n][i]
        idx = i
        cnt = d[n][i]
    elif dp[n][i] * idx == ans * i:
        cnt += d[n][i]
print(ans / idx)
print(cnt)
