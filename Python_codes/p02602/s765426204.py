import numpy as np
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = np.prod(a[:k])
for i in range(k, n):
  c = a[i - k]
  d = a[i]
  if c < d:
    print('Yes')
  else:
    print('No')
  b = b * d // c