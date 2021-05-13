mod = 10 ** 9 + 7
s = input()
n = len(s)
dp = [[0] * 13 for _ in range(n + 1)]
dp[0][0] = 1

numbers = list(range(10))
for i in range(n):
    next_nums = numbers if s[i] == '?' else [int(s[i])]
    for j in range(13):
        for k in next_nums:
            jj = (10 * j + k) % 13
            dp[i + 1][jj] = (dp[i + 1][jj] + dp[i][j]) % mod
print(dp[n][5])

