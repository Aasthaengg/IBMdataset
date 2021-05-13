import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

N = int(input())
color = [-1]*N
graph = [[] for _ in range(N)]
for _ in range(N-1):
  u, v, w = map(int, input().split())
  u -= 1
  v -= 1
  graph[u] += [[v, w]]
  graph[v] += [[u, w]]

def dfs(u, c):
  color[u] = c
  for v, w in graph[u]:
    if color[v] == -1:
      if w % 2 == 0:
        dfs(v, c)
      else:
        dfs(v, abs(1-c))
  return

dfs(0, 0)
color = list(map(str, color))
print(*color)

