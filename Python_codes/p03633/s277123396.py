import numpy as np
n = int(input())
lst = []
for i in range(n):
  lst.append(int(input()))
res = 1
for i in range(n):
  res = np.lcm(res, lst[i])
print(res)