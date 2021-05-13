k=int(input())
l=list(range(1, k+1))
import itertools
import math
from functools import reduce
def gcd(*numbers):
  return reduce(math.gcd, numbers)
ans=0
for v in itertools.combinations_with_replacement(l, 3):
  if v[0]==v[1]==v[2]:
    ans+=gcd(*v)
  elif v[0]==v[1]:
    ans+=gcd(*v)*3
  elif v[1]==v[2]:
    ans+=gcd(*v)*3
  elif v[0]==v[2]:
    ans+=gcd(*v)*3
  else:
    ans+=gcd(*v)*6
print(ans)