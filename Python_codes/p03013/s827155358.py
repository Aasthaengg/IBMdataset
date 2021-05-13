n, m = map(int, input().split())
broken = [0]*(n+1)
#m個階段が壊れているからそれをbrokenに入れる
for i in range(m):
    a = int(input())
    broken[a] = 1
dp = [0]*(n+1)
dp[0] = 1
mod = 1000000007
for i in range(1, n+1):
    if broken[i]:
        continue
    #dp[-1]は0だから上手く回る
    dp[i] = (dp[i-1] + dp[i-2]) % mod
print(dp[n])
