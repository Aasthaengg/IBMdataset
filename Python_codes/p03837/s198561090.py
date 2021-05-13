import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix

N, M = map(int, input().split())

mp = [[100000 for i in range(N)] for j in range(N)]
mp2 = []
for i in range(M):
  a,b,c = map(int, input().split())
  mp[a-1][b-1] = c
  mp[b-1][a-1] = c
  mp2.append([a,b,c])
  
D = shortest_path(np.array(mp))

ans = [1 for i in range(M)]
for i,edge in enumerate(mp2):
  #print("{} {}".format(D[edge[0]-1, edge[1]-1], edge[2]))
  if D[edge[0]-1, edge[1]-1] >= edge[2]:
    ans[i] = 0
    
print(sum(ans))