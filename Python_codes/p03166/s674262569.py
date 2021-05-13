import sys
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)

dp = [-1]*n

def DFS(node):
    ma = -1
    for c_node in graph[node]:
        if dp[c_node]>=0:
            tmp = dp[c_node]
        else:
            tmp = DFS(c_node)
        if tmp > ma:
            ma = tmp
    dp[node] = ma+1
    return ma+1

sys.setrecursionlimit(10**9)

for i in range(n):
    if dp[i]>=0:
        continue
    DFS(i)
print(max(dp))