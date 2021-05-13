n = int(input())
m = [9 ** i for i in range(6)]
m += [6 ** i for i in range(1, 7)]
m.sort()
dp = [float("inf") for i in range(n + 1)]
dp[0] = 0
for i in range(n):
    for j in m:
        if i + j <= n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)
print(dp[-1])