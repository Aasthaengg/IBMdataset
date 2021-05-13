#from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
import copy
N = int(input())

A = []
for _ in range(N):
  A.append(list(map(int, input().split())))
  
D = copy.deepcopy(A)
for i in range(N):
  D[i][i] = 0
  
for k in range(N):
  for i in range(N):
    for j in range(N):
      D[i][j] = min(D[i][j], D[i][k] + D[k][j])
      
#G = csgraph_from_dense(A)
#D = floyd_warshall(G)

ans = 0
for i in range(N):
  for j in range(i+1,N):
    if D[i][j] < A[i][j]:
      print(-1)
      exit(0)
      
for i in range(N):
  for j in range(i+1,N):
    flg = True
    for k in range(N):
      if i == k or j == k:
        continue
      if D[i][j] == D[i][k] + D[k][j]:
        flg = False
    if flg:
      ans += D[i][j]
      
print(int(ans))