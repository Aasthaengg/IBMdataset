from sys import setrecursionlimit
setrecursionlimit(10 ** 5 + 10)

N, M, *XY = map(int, open(0).read().split())

E = [[] for _ in range(N + 1)]
for x, y in zip(*[iter(XY)] * 2):
    E[x].append(y)

memo = {}
def dp(p):
    if p not in memo:
        memo[p] = max((1 + dp(c) for c in E[p]), default=0)
    return memo[p]

print(max(dp(p) for p in range(1, N + 1)))