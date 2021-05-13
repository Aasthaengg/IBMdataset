n, m = map(int, input().split())
parents = [[] for _ in range(n)]
outdegree = [0] * n
indegree = [0] * n
path_root = [0] * n
for _ in range(m):
  x, y = map(int, input().split())
  x -= 1
  y -= 1
  parents[y].append(x)
  outdegree[x] += 1
  indegree[y] += 1
stack = [i for i in range(n) if outdegree[i] == 0]
while stack:
  vertex = stack.pop()
  path_length = path_root[vertex] + 1
  for parent in parents[vertex]:
    outdegree[parent] -= 1
    indegree[vertex] -= 1
    path_root[parent] = max(path_root[parent], path_length)
    if outdegree[parent] == 0:
      stack.append(parent)
print(max(path_root))