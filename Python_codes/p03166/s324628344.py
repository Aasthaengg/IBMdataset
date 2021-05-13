def li():
    return [int(x) for x in input().split()]

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

INF = 10 ** 60

G = defaultdict(list)

N, M = li()

for _ in range(M):
    x, y = li()
    G[x].append(y)

dp = [-1] * (10 ** 5 + 1)

def dfs(v):
    if dp[v] != -1:
        return dp[v]
    ret = 0
    for cv in G[v]:
        ret = max(ret, dfs(cv) + 1)
    dp[v] = ret
    return ret


ans = 0
for v in range(1, N+1):
    # print(dfs(v))
    ans = max(ans, dfs(v))

print(ans)