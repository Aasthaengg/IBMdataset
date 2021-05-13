s = list(input())
n = len(s)
mod = pow(10, 9) + 7
dp = [[0] * 13 for _ in range(n)]
if s[-1] == "?":
    for i in range(10):
        dp[-1][i] = 1
else:
    dp[-1][int(s[-1])] = 1
digit = 1
for i in range(n - 2, -1, -1):
    digit *= 10
    digit %= 13
    if s[i] == "?":
        for j in range(10):
            x = (j * digit) % 13
            for k in range(13):
                dp[i][k] += dp[i + 1][(k - x) % 13]
                dp[i][k] %= mod
    else:
        x = (int(s[i]) * digit) % 13
        for k in range(13):
            dp[i][k] = dp[i + 1][(k - x) % 13]
ans = dp[0][5]
print(ans)