N = int(input())

dp = [2, 1]

for l in range(2, N + 1):
    dp.append(dp[l - 1] + dp[l - 2])

print(dp[-1])
