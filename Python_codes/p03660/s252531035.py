from collections import deque

N = int(input())
tree = [[] for i in range(N)]
for i in range(N-1):
  a, b = map(int, input().split())
  a -= 1; b -= 1
  tree[a].append(b); tree[b].append(a)

def calc_dist(node):
  dist = [-1] * N
  dist[node] = 0
  d = deque([[node, -1]])
  while d:
    node, p = d.pop()
    children = tree[node]
    for child in children:
      if child == p:
        continue
      dist[child] = dist[node] + 1
      d.append([child, node])
  return dist

d1 = calc_dist(0)
dN = calc_dist(N-1)

fennec = snuke = 0
for node in range(1, N-1):
  if d1[node] <= dN[node]:
    fennec += 1
  else:
    snuke += 1

if fennec > snuke:
  print('Fennec')
else:
  print('Snuke')