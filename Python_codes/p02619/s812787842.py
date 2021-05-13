import numpy as np

D = int(input())
c = np.array( list(map(int, input().split())) )
s = [[] for i in range(365+1)]
for i in range(D):
  s[i] = list(map(int, input().split()))
#
last = np.array( [-1]*26 )

v = 0
for d in range(D):
  t =  int(input())
  t -= 1
  last[t] = d
  v += s[d][t]
  v -= sum( (d-last)*c )
  print(v)
#
