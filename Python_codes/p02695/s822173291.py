import itertools
import numpy as np
d_list = []
sum_d = 0
N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for i in range(Q)]
ans = 0
A = [1 for i in range(N)]
for A in itertools.combinations_with_replacement(range(1, M+1), N):
  for i in range(Q):
    a = abcd[i][0]
    b = abcd[i][1]
    c = abcd[i][2]
    d = abcd[i][3]
    if A[b-1]-A[a-1] == c:
      d_list.append(abcd[i][3])
  if sum_d <= sum(d_list):
    sum_d = sum(d_list)
  d_list.clear()
print(sum_d)