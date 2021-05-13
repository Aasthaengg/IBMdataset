import sys
sys.setrecursionlimit(2147483647)
INF = float("inf")
MOD = 10**9 + 7 # 998244353
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n, m = map(int, input().split())
    E = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        E[u].append(v)
        indeg[v] += 1

    # topological sort
    stack = [v for v in range(n) if indeg[v] == 0]
    order = []
    while stack:
        v = stack.pop()
        order.append(v)
        for nv in E[v]:
            indeg[nv] -= 1
            if indeg[nv] == 0:
                stack.append(nv)

    dp = [0] * n
    for v in order[::-1]:
        for nv in E[v]:
            dp[v] = max(dp[v], 1 + dp[nv])

    print(max(dp))
resolve()