import numpy as np
X,N = map(int,input().split())
P = list(map(int,input().split()))
A = []

for n in range(102):
  if n not in P:
    A+=[abs(n-X)]
  else:
    A+=[100]

print(np.argmin(A))