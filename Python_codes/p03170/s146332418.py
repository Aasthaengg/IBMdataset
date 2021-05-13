n, k = map(int, input().split())
ns = list(map(int, input().split()))
dp = [0] * (k + 1)
for i in range(k + 1):
    dp[i] = not all(dp[i - s] for s in ns if i - s >= 0)
print(['Second', 'First'][dp[-1]])