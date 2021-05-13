import numpy as np
n = int(input())
V = list(map(float, input().split()))

V = np.array(sorted(V))
for i in range(1, n):
  V[:i+1] = V[:i+1] /2
print(np.sum(V))