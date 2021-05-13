import numpy as np
n, k = map(int,input().split())
gates = [0]*(n+1)
for i in range(k):
  l,r = map(int,input().split())
  gates[l-1] += 1
  gates[r] -= 1
print(np.count_nonzero(np.cumsum(gates) == k))
