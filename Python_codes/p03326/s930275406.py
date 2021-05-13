import numpy as np
import itertools
N, M = map(int, input().split())
if M == 0:
  print(0)
else:
  data = []
  for i in range(N):
    data.append(list(map(int, input().split())))
  data = np.array(data, dtype='int64')

  results = []
  for op in itertools.product([-1, 1], repeat=3):
    vals = (data * op).sum(axis=1)
    vals.sort()
    results.append(vals[-M:].sum())

  print(max(results))