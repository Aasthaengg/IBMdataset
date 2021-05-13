N, M = map(int, input().split())
C = tuple(map(int, input().split()))

inf = 10**18
dp = [inf] * (N + 10)
dp[0] = 0

for c in C:
    for i in range(c, N + 1):
        dp[i] = min(dp[i], dp[i - c] + 1)
ans = dp[N]
print(ans)
