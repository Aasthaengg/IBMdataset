n = int(input())
p = [int(input()) for _ in range(n)]

#dp[i]はiで終わる連続整数長
dp = [0 for _ in range(n+1)]
for i in range(n):
    dp[p[i]] = dp[p[i] - 1] + 1

print(n - max(dp))