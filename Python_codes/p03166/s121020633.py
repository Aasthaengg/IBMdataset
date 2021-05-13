import sys
sys.setrecursionlimit(10**8)
N, M = map(int, input().split())
G = dict([[i, []] for i in range(N)])
for _ in range(M):
    x, y = map(int, input().split())
    G[x-1].append(y-1)

dp = [-1] * N


def rec(v):
    if dp[v] >= 0:
        return dp[v]
    if len(G[v]) == 0:
        return 0

    ret = -1
    for nv in G[v]:
        ret = max(ret, rec(nv) + 1)

    dp[v] = ret
    return ret


print(max([rec(v) for v in range(N)]))
