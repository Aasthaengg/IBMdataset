from math import gcd
from functools import reduce

N = int(input())

ans = 0
for i in range(1, N+1):
  for j in range(1, N+1):
    for k in range(1, N+1):
      ans += reduce(gcd, [i, j, k])

print(ans)