from scipy.sparse.csgraph import floyd_warshall

N, M, L = map(int, input().split())
INF = 10**9 + 1
dist = [[0 if i == j else INF for i in range(N+1)] for j in range(N+1)]
for i in range(M):
  a, b, c = map(int, input().split())
  dist[a][b] = c
  dist[b][a] = c

dist = floyd_warshall(dist)

dist_2 = [[INF for i in range(N+1)] for j in range(N+1)]
for i in range(1, N+1):
  for j in range(i+1, N+1):
    if dist[i][j] <= L:
      dist_2[i][j] = 1
      dist_2[j][i] = 1

dist_2 = floyd_warshall(dist_2)

Q = int(input())
for i in range(Q):
  s, t = map(int, input().split())
  print(-1 if dist_2[s][t] == INF else int(dist_2[s][t]-1))
