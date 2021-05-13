n, m = map(int, input().split())
c = list(map(int, input().split()))
inf = 10 ** 7

dp = [inf for _ in range(n+1)]
dp[0] = 0
for i in range(1, n+1):
    for j in range(m):
        if i - c[j] >= 0:
            dp[i] = min(dp[i], dp[i-c[j]] + 1)

print(dp[n])
