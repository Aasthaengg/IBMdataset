import sys


def resolve():
    sys.setrecursionlimit(10 ** 6)
    readline = sys.stdin.readline
    
    def rec(v: int):
        """メモ化再帰"""
        if dp[v] != -1:
            return dp[v]
        res = 0
        for nv in G[v]:
            res = max(res, rec(nv) + 1)
        dp[v] = res
        return dp[v]

    N, M = map(int, readline().split())
    G = [[] for _ in [0] * N]
    for _ in [0] * M:
        x, y = map(int, readline().split())
        G[x - 1].append(y - 1)

    # メモ化再帰
    dp = [-1] * N
    res = 0
    for v in range(N):
        res = max(res, rec(v))
    print(res)


resolve()
