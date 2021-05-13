n, m = map(int, input().split())
ok = [1] * n
for i in range(m):
    x = int(input())
    ok[x-1] = 0
mod = 1000000007
dp = [0] * (n+2)
dp[1] = 1
for i in range(n):
    dp[i+2] = (dp[i+1] + dp[i])%mod if ok[i] else 0

print(dp[n+1])