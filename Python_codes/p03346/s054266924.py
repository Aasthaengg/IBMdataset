n = int(input())
p = [int(input()) for _ in range(n)]

dp = [0] * (n + 1)
for e in p:
    dp[e] = dp[e-1] + 1

ans = n - max(dp[1:])
print(ans)
