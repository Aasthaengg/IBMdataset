import sys
input = lambda: sys.stdin.readline().rstrip()
mod = 998244353
n, s = map(int, input().split())
a = [int(x) for x in input().split()]
dp = [[0]*(s + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(s + 1):
        dp[i][j] += dp[i - 1][j]*2
        dp[i][j] %= mod
        if j - a[i - 1] >= 0:
            dp[i][j] += dp[i - 1][j - a[i - 1]]
            dp[i][j] %= mod
print(dp[-1][-1])