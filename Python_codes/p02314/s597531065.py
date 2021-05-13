n, m = map(int, input().split())

C = list(map(int, input().split()))

# nまで
dp = [float('inf')] * (n + 1)
dp[0] = 0
for i in range(m):
    for j in range(n + 1):
        if j >= C[i]:
            dp[j] = min(dp[j - C[i]] + 1, dp[j])

print(dp[n])

