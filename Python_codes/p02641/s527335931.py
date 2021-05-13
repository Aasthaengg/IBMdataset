import numpy as np
X,N = map(int, input().split())


if N == 0:
  print(X)
else:
  ans_v = 102
  ans_idx = 0
  candidate = list(np.arange(0,102))
  p = list(map(int, input().split()))
  for i in range(N):
    candidate.remove(p[i])
  for i in range(len(candidate)):
    if ans_v > abs(X-candidate[i]):
      ans_v = abs(X-candidate[i])
      ans_idx = i
  print(candidate[ans_idx])
