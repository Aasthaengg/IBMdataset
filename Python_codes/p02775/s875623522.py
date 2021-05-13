s = list(input())
s.reverse()
s.append('0')

dp = [[1000000000] * 2 for _ in range(1000005)]
dp[0][0] = 0
n = len(s)
for i in range(n):
    for j in range(2):
        x = int(s[i])
        x += j
        if x < 10:
            dp[i + 1][0] = min(dp[i + 1][0], dp[i][j] + x)
        if x > 0:
            dp[i + 1][1] = min(dp[i + 1][1], dp[i][j] + (10 - x))

ans = dp[n][0]
print(ans)