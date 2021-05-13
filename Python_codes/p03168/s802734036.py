import sys
sys.setrecursionlimit(2147483647)
INF = float("inf")
MOD = 10**9 + 7 # 998244353
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    for p in map(float, input().split()):
        ndp = [0] * (n + 1)
        for i in range(n):
            ndp[i + 1] += dp[i] * p
        for i in range(n):
            ndp[i] += dp[i] * (1 - p)
        dp = ndp

    res = 0
    for i in range(n + 1):
        if 2 * i > n:
            res += dp[i]
    print(res)
resolve()