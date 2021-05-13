import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n, p = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [1, 0]
    for a in A:
        if a & 1:
            s = sum(dp)
            dp = [s, s]
        else:
            dp = [dp[0] * 2, dp[1] * 2]

    print(dp[p])
resolve()