import math
N, K = list(map(lambda k: int(k), input().split(" ")))
A = list(map(lambda a: int(a), input().split(" ")))

pos_of_1 = A.index(1)

if K >= pos_of_1 + 1 or N - K <= pos_of_1:
  print(math.ceil((N - K) / (K - 1)) + 1) 
else:
  L = A[:pos_of_1 + 1]
  R = A[pos_of_1:]
  res = []
  for i in range(1, K):
    l = math.ceil((len(L) - i) / (K - 1)) + 1
    r = math.ceil((len(R) - K - 1 + i) / (K - 1)) + 1
    res.append(l + r - 1)
  print(min(res))