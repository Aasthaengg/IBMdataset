import numpy as np
N, K, Q = input().split(' ')
N = int(N)
K = int(K)
Q = int(Q)
P = np.ones(N) * K
for i in range(Q):
  A = int(input())
  P[A-1] += 1
P -= Q
for i in range(N):
  if P[i] > 0:
    print('Yes')
  else:
    print('No')