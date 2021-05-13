import sys
sys.setrecursionlimit(10000)
dp = []
coins = []
INF = 9999999

def change(n, m):
    if n == 0:
        return 0
    if dp[n] == INF:
        res = INF
        for j in range(0, m):
            if n - coins[j] >= 0:
                res = min(res, change(n - coins[j], m) + 1)
        dp[n] = res
    return dp[n]

line = input()
n, m = list(map(int, line.split()))
line = input()
d = list(map(int, line.split()))
coins = sorted(d)
coins.reverse()
dp = [INF] * (n + 1)
change(n, m)
print(dp[n])
