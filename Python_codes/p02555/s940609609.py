S = int(input())

dp = [0] * (S + 1)
dp[0] = 1
for i in range(3, S + 1):
    dp[i] = sum(dp[:i - 2])

print(dp[S] % (10 ** 9 + 7))
