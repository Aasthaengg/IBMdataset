import sys
from collections import defaultdict as dd
sys.setrecursionlimit(4100000)

def dfs(node):
  visited[node-1] = True
  
  for next_node in tree[node]:
    if visited[next_node-1]:
      continue
    counter[next_node-1] += counter[node-1]
    dfs(next_node)

N, Q = map(int, input().split())
tree = dd(list)
visited = [False] * N
counter = [0] * N
operation = []
for _ in range(N-1):
  a, b = map(int, input().split())
  tree[a].append(b) 
  tree[b].append(a) 
for _ in range(Q):
  operation.append(tuple(map(int, input().split())))
  
for p, x in operation:
  counter[p-1] += x
dfs(1)
print(*counter)