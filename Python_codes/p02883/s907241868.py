import sys
readline = sys.stdin.readline

import numpy as np

N,K = map(int,readline().split())
A = np.sort(np.array(readline().split(), dtype = int))
F = np.sort(np.array(readline().split(), dtype = int))[::-1]

# X秒で完食できるか二分探索

ng = -1
ok = F[0] * A[-1]

def isOk(x):
  return A.sum() - np.minimum(A, x // F).sum() <= K
  
while abs(ok - ng) > 1:
  mid = abs(ok + ng) // 2
  if isOk(mid):
    ok = mid
  else:
    ng = mid
    
print(ok)

