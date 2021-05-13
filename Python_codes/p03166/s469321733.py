import sys
sys.setrecursionlimit(10000)
# Longest path
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)
dp = [-1 for _ in range(N)]

def rec(c):
    if dp[c] != -1:
        return dp[c]
    res = 0
    for i in graph[c]:
        res = max(res, rec(i) + 1)
    dp[c] = res
    return res

for i in range(N):
    rec(i)
print(max(dp))