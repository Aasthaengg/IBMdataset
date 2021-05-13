n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]
dpsum = [[0] * (m + 1) for _ in range(n + 1)]
mod = pow(10, 9) + 7
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = 1
            if not i == 1 and not j == 1:
                dp[i][j] += dpsum[i - 1][j - 1]
                dp[i][j] %= mod
        dpsum[i][j] = dpsum[i - 1][j] + dpsum[i][j - 1] - dpsum[i - 1][j - 1] + dp[i][j]
        dpsum[i][j] %= mod
ans = dpsum[n][m] + 1
print(ans)