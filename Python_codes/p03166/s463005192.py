import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = [int(x) for x in input().split()]
g = [[] for _ in range(n)]
for _ in range(m):
    x, y = [int(x) for x in input().split()]
    g[x - 1].append(y - 1)

memo = [-1]*n

def dp(v):
    if memo[v] >= 0:
        return memo[v]
    else:
        res = 0
        for u in g[v]:
            res = max(res, dp(u) + 1)
        memo[v] = res
        return res

for i in range(n):
    dp(i)
print(max(memo))


