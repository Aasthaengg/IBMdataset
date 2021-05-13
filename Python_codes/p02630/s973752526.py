import numpy as np
import collections

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
P = [list(map(int,input().split())) for i in range(Q)]
A = np.array(A)

sum_A = np.sum(A)
c = collections.Counter(A)
  
for item in P:
  if item[0] in c.keys():
    sum_A += ((item[1] - item[0]) * c[item[0]])
    if item[1] in c.keys():
      c[item[1]] += c[item[0]]
    else:
      c[item[1]] = c[item[0]]
    c.pop(item[0])
  print(sum_A)
