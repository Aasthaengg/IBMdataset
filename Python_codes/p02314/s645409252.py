n, m = map(int, input().split())
C = list(map(int, input().split()))
dp = [-1] * (n+1)

for c in C:
    if c <= n:
        dp[c] = 1

for p in range(1, n+1):
    for c in C:
        if p-c < 0 or dp[p-c] < 0:
            continue
        dp[p] = min(dp[p], dp[p-c] + 1) if dp[p] > 0 else dp[p-c] + 1

# print(*dp)
print(dp[n])

