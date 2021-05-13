import numpy as np
N, K = map(int,input().split())
B = []
C = np.zeros(N)
e = 0
for i in range(K):
  d = int(input())
  A = list(map(int,input().split()))
  for j in range(1, N + 1):
    B.append(A.count(j))
  for k in range(N):
    C[k] += B[k] 
  B = []
for l in range(N):
  if C[l] == 0:
    e += 1
print(e)
