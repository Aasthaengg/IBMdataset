def ints():
  return [int(x) for x in input().split()]
def ii():
  return int(input())

import math

N, K = ints()
A = list(sorted(ints()))
F = list(reversed(sorted(ints())))
AF = [A[i]*F[i] for i in range(N)]

afmax = max(AF)

def can(seiseki):
  k = K
  for i in range(N):
    af = AF[i]
    if af>seiseki:
      k -= math.ceil((af-seiseki)/F[i])
      if k<0:
        return False
  return k>=0

l = -1
r = afmax
while r-l>1:
  m = (l+r)//2
  if can(m):
    r = m
  else:
    l = m
print(r)

