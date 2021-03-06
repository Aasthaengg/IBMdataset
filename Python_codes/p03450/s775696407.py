# 人を頂点と見なしたグラフを作る。有向で、逆向きの場合は正負を反転させて辺を張る
# 頂点からの距離を記録し、一致しない箇所があればNG。
# 全ての辺を通るまで続ける。
# 辺の情報を[{0から行ける頂点},{1から行ける頂点},...]で管理する
# 親には進まないようにしてDFSする

N,M = map(int,input().split())
E = [[] for i in range(N)]
for i in range(M):
  L,R,D = map(int,input().split())
  E[L-1].append([R-1,D])
  E[R-1].append([L-1,-D])
from collections import deque
# 頂点、親、距離
INF = 10 ** 10
dist = [INF] * N
for i in range(N):
  if dist[i] != INF:
    continue
  dist[i] = 0
  q = deque()
  q.append(i)
  while q:
    v = q.popleft()
    for child in E[v]:
      if dist[child[0]] == INF:
        dist[child[0]] = dist[v] + child[1]
        q.append(child[0])
      else:
        if dist[child[0]] != dist[v] + child[1]:
          print("No")
          exit(0)
else:
  print("Yes")
