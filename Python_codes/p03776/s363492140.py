N,A,B = map(int,input().split())
V = [int(x) for x in input().split()]

V.sort(reverse = True) # desc order

x = V[A-1]
large = V.index(x) # xより大きなものの個数
cnt = V.count(x)

import numpy as np
comb = np.zeros((N+1,N+1),dtype=np.int64)
comb[:,0] = 1
for n in range(1,N+1):
  comb[n,1:] = comb[n-1,1:] + comb[n-1,:-1]

max_avg = sum(V[:A]) / A
pattern = 0
if V[0] == V[A-1]:
  for choose in range(A-large, B-large+1):
    pattern += comb[cnt,choose]
else:
  pattern = comb[cnt,A-large]
  
print(max_avg)
print(pattern)