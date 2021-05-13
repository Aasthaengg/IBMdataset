import sys
INF = 1 << 60
MOD = 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n, s = map(int, input().split())
    dp = [0] * (s + 1)
    dp[0] = 1
    res = 0
    A = list(map(int, input().split()))
    for a in A:
        ndp = [2 * t % MOD for t in dp]
        if s >= a:
            for i in range(s - a, -1, -1):
                ndp[i + a] += dp[i]
                ndp[i + a] %= MOD
        dp = ndp


    print(dp[s] % MOD)
resolve()