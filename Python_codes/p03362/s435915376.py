import numpy as np
U = 55556
T = np.zeros(U)
T[2] = 1
T[3::2] = 1
for i in range(3,U,2):
  if i*i>U:
    break
  if T[i]:
    T[i*i::2*i] = 0
pls = np.where(T)[0]
N = int(input())
ans = []
for p in pls:
  if p%5==1:
    ans += [str(p)]
  if len(ans)==N:
    break
print(' '.join(ans))