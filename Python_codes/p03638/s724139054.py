import numpy as np
H, W, N, *A = map(int, open(0).read().split())
ls = []
for i in range(N):
  ls += [i+1]*A[i]
ls = np.array(ls)
ls = ls.reshape((H,W))
ls[1::2] = ls[1::2,::-1]
for a in ls:
  print(*a)
