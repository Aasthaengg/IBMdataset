n,m = map(int,input().split())
a = []
stairs = [0]*(n+2)
for _ in range(m):
    a = int(input())
    stairs[a] = 1
mod = 10**9 + 7

dp = [0]*(n+2)
dp[0] = 1

for i in range(n):
    if i <= 1:
        if stairs[i+1] == 0:
            dp[i+1] += dp[i]
            dp[i+1] %= mod
            stairs[i+1] = 1
    if stairs[i+2] == 0:
        dp[i+2] += dp[i+1]+dp[i]
        dp[i+2] %= mod
        stairs[i+2] = 1

print(dp[n]%mod)
