import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

N,M,L = map(int,readline().split())
ABC = [list(map(int,readline().split())) for _ in range(M)]
Q = int(readline())
ST = [list(map(int,readline().split())) for _ in range(Q)]
    
def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

INF = 10**11
d = [[INF]*N for i in range(N)] 
a =  [[INF]*N for i in range(N)] 
for x,y,z in ABC:
    if z <= L:
      d[x-1][y-1] = z
      d[y-1][x-1] = z
for i in range(N):
    d[i][i] = 0
    a[i][i] = 1
d = csr_matrix(d)
d = floyd_warshall(csgraph=d)

for i in range(N-1):
  for j in range(i+1,N):
    if d[i][j] <= L:
      a[i][j] = 1
      a[j][i] = 1
a = csr_matrix(a)
a = floyd_warshall(csgraph=a)

for s,t in ST:
  ans = a[s-1][t-1]
  if ans == INF:
      print(-1)
  else:
      print(int(ans)-1)