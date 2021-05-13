import numpy as np

N = int(input())
for h in range(1, 3501):
  n = np.arange(1, 3501, dtype=np.int64)
  num = N*h*n
  den = 4*h*n - N*n - N*h
  n = n[(den>0) & (num%den == 0)]
  if len(n) > 0:
    n = n[0]
    w = N*h*n // (4*h*n - N*n - N*h)
    break
print(n, h, w)