import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import numpy as np

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

n = int(readline())
f = []
A = []
chk = []
for i in range(n):
  ar = list(map(int,readline().split()))
  f.append(ar)
  for j,ai in enumerate(ar):
    if i == j:
      continue
    A.append((i,j,ai))
  
INF = 10**9+1
g = [[INF] * n for _ in range(n)]
for a,b,c in A:
    g[a][b] = c
    g[b][a] = c

g = csr_matrix(g)
d = floyd_warshall(csgraph=g)

t = f == d
if t.all():
  ans = 0
  for i in range(n):
    d[i,i] = INF

  for i in range(n):
    for j in range(i+1,n):
      opt = np.min(d[i] + d[j])
      if opt > d[i,j]:
        ans += d[i,j]
        
  print(int(ans))
else:
  print(-1)