import numpy as np
N = int(input())
F = [[int(x) for x in input().split()] for _ in range(N)]
P = [[int(x) for x in input().split()] for _ in range(N)]

import itertools
answer = -(10 ** 18)
for a in itertools.product([0,1], repeat = 10):
  if sum(a) == 0:
    continue
  profit = 0
  for shop in range(N):
    profit += P[shop][sum(a[i]*F[shop][i] for i in range(10))]
  if answer < profit:
    answer = profit

print(answer)
  
