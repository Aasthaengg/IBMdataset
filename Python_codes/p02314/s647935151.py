n, m = map(int, input().split())
*c, = map(int, input().split())
c.sort()
dp = [2**32 for _ in range(n+1)]
for i in range(n+1):
    dp[i] = i
for i in range(1, m):
    for j in range(n+1):
        if (j-c[i]) >= 0:
            dp[j] = min([
                dp[j],
                dp[j-c[i]]+1
            ])
        else:
            dp[j] = dp[j]
print(dp[n])

