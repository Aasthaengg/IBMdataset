import numpy as np
N, M = list(map(int,input('').split(' ')))
A = np.array(sorted(list(map(int,input('').split(' '))), reverse=True))
pts = np.sum(A)
if A[M-1]>=(pts/(4*M)):
  print('Yes')
else:
  print('No')