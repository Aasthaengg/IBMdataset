import sys
sys.setrecursionlimit(10**7)
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    edge[x-1].append(y-1)
dp = [0]*N
def f(v):
    if dp[v] != 0:
        return dp[v]
    res = 0
    for i in edge[v]:
        res = max(res, f(i)+1)
    dp[v] = res
    return res
for i in range(N):
    f(i)
print(max(dp))