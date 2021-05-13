import math
from decimal import Decimal
import itertools

N = int(input())
x, y = [0] * N, [0] * N
per = list(itertools.permutations(range(1, N+1)))
for i in range(N):
  x[i], y[i] = map(int, input().split())
dis = 0
for lis in per:
  for j in range(1, len(lis)):
    k = lis[j]
    l = lis[j-1]
    dis += math.sqrt((x[l-1] - x[k-1])**2 + (y[l-1] - y[k-1])**2)
fac = math.factorial(N)
print(dis/fac)