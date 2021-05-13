from fractions import gcd
from functools import reduce
N,K,*A = map(int, open(0).read().split())
g = reduce(gcd,A)
a = max(A)
if a>=K and K%g==0:
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')