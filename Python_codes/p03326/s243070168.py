import numpy as np
import sys
read = sys.stdin.read
n, m = map(int, input().split())
xyz = np.array(read().split(), dtype=np.int64).reshape(n, 3).T
ans = 0
for i in range(2):
  for j in range(2):
    for k in range(2):
      L = np.array([xyz[0] * (-1)**i, xyz[1] * (-1)**j, xyz[2] * (-1)**k])
      A = L.sum(axis=0).tolist()
      t = sum(sorted(A, reverse=True)[:m])
      ans = max(ans, t)
print(ans)