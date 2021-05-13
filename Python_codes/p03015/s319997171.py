import sys
input = lambda: sys.stdin.readline().rstrip()
mod = 10**9 + 7
l = input()
n = len(l)
dp = [[0, 0] for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    num = l[i - 1]
    if num == "1":
        dp[i][0] = dp[i - 1][0]*2
        dp[i][1] = dp[i - 1][1]*3 + dp[i - 1][0]
    else:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]*3
    dp[i][0] %= mod
    dp[i][1] %= mod
print(sum(dp[-1]) % mod)