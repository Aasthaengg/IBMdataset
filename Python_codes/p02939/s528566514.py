s = input()
n = len(s)
dp = [0] * n
dp[0] = 1

for i in range(1, n):
    if s[i] != s[i - 1]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i - 1]
        if i >= 2:
            dp[i] = max(dp[i], dp[i - 2] + 1)
        if i >= 3:
            dp[i] = max(dp[i], dp[i - 3] + 2)
print(dp[-1])