import sys
sys.setrecursionlimit(20000000)
input = sys.stdin.readline
n = int(input())
a = [int(input()) for i in range(n)]
mod = 10**9+7
dp = [0]*(n+1)
mae = [-2]*(max(a)+1)
mae2 = [0]*(max(a)+1)
dp[0] = 1
for i in range(n):
        if mae[a[i]] != -2 and mae[a[i]] != i-1:
                dp[i+1] = dp[i] + mae2[a[i]]
        else:
                dp[i+1] = dp[i]
        dp[i+1] %= mod
        if mae[a[i]] == i-1:
                mae[a[i]] = i
                continue
        mae[a[i]] = i
        mae2[a[i]] += dp[i]
        mae2[a[i]] %= mod
print(dp[n]%mod)