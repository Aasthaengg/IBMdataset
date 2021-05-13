import numpy as np
import copy
import math
n, kk = map(int, input().split())
a = [int(x) for x in input().split()]
a2 = np.array(copy.deepcopy(a))

key = 1
p = int(math.log2(max([kk, 1])))+1
x = [1]*p
for i in range(p):
  k = np.sum(a2%2)
  if n >= 2*k:
    x[i] = 0
  a2 = a2//2

x_sum = 0
for i in range(p-1, -1, -1):
  if x[i]:
    continue
  if x_sum+pow(2, i) > kk:
    continue
  x_sum += pow(2, i)

ans = 0
for i in range(n):
  ans += (x_sum^a[i])
print(ans)