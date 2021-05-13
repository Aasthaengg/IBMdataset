n = int(input())

dp = [float('inf')] * (n + 1)
dp[0] = 0


for i in range(n):
    dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    for j in range(n):
        if i + 6 ** (j + 1) <= n:
            dp[i + 6 ** (j + 1)] = min(dp[i + 6 ** (j + 1)], dp[i] + 1)
        else:
            break
    for k in range(n):
        if i + 9 ** (k + 1) <= n:
            dp[i + 9 ** (k + 1)] = min(dp[i + 9 ** (k + 1)], dp[i] + 1)
        else:
            break

print(dp[n])