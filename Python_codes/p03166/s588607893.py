import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
dp = [-1 for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)

def rec(v):
    if dp[v] >= 0:
        return dp[v]
    temp = 0
    for next in graph[v]:
        temp = max(rec(next) + 1, temp)
    dp[v] = temp
    return temp

for i in range(N):
    rec(i)
print(max(dp))