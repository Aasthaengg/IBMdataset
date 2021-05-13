INF = pow(10, 15)

def main():
  n, m, p = map(int, input().split())
  edges = []
  for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a-1, b-1, p-c))  # 辺の重みの正負反転（最長路→最短路にしたいので）

  dist = [INF for _ in range(n)]
  frome = [-1 for _ in range(n)]
  dist[0] = 0
  for _ in range(n):
    for edge in edges:
      if dist[edge[0]] == INF:
        continue
      if dist[edge[1]] > dist[edge[0]] + edge[2]:
        dist[edge[1]] = dist[edge[0]] + edge[2]
        frome[edge[1]] = edge[0]

  for i, edge in enumerate(edges):
    if dist[edge[1]] > dist[edge[0]] + edge[2]:
      edges[i] = (edge[0], edge[1], -INF)

  dist = [INF for _ in range(n)]
  frome = [-1 for _ in range(n)]
  dist[0] = 0
  for _ in range(n):
    for edge in edges:
      if dist[edge[0]] == INF:
        continue
      if dist[edge[1]] > dist[edge[0]] + edge[2]:
        dist[edge[1]] = dist[edge[0]] + edge[2]
        frome[edge[1]] = edge[0]

  fromd = {}
  f = n-1
  while frome[f] != -1:
    if f in fromd:
      break
    fromd[f] = frome[f]
    f = frome[f]

  is_loop = False
  for edge in edges:
    if dist[edge[1]] > dist[edge[0]] + edge[2]:
      if edge[0] in fromd:
        is_loop = True
        break

  if is_loop:
    print(-1)
  else:
    if dist[-1] > 0:
      print(0)
    else:
      print(-dist[-1])


if __name__ == '__main__':
  main()
