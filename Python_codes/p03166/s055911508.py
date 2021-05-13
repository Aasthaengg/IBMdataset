
import sys
sys.setrecursionlimit(10**9)

def dfs(i):
    if distance[i] != -1:
        return distance[i]
    ans = 0
    for node in graph[i]:
        ans = max(ans, dfs(node) + 1)
    distance[i] = ans
    return ans

n, m = map(int, input().split())

graph = [[] for i in range(n)]
distance = [-1 for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)

ans = 0
for i in range(n):
    ans = max(ans, dfs(i))

print(ans)