class Edge:
  def __init__(self, starting_point, arrival_point, cost):
    self.starting_point = starting_point
    self.arrival_point = arrival_point
    self.cost = cost

def solve():
  N, M, P = map(int, input().split())
  edges = []
  INF = float('inf')
  dist = [INF for _ in range(N + 10)]
  dist[1] = 0
  for i in range(M):
    a, b, c = map(int, input().split())
    e = Edge(a, b, -c + P)
    edges.append(e)
  for i in range(2 * N):
    for e in edges:
      if dist[e.arrival_point] > e.cost + dist[e.starting_point]:
        dist[e.arrival_point] = e.cost + dist[e.starting_point]
        if i == N - 1:
          dist[e.arrival_point] = -INF
  if dist[N] != -INF:
    return max(-dist[N], 0)
  else:
    return -1
print(solve())