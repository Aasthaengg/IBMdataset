import numpy as np
n = int(input())
a = np.array(list(map(int, input().split())))
if len(np.unique(a)) == len(a):
  print('YES')
else:
  print('NO')