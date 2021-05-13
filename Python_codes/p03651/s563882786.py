from math import gcd
from functools import reduce
n,k = map(int,input().split())
a = sorted(list(map(int,input().split())))

def mgcd(l):
  return reduce(gcd,l)
if k in a:
  print("POSSIBLE")
  exit()
if a[-1]<k:
  print("IMPOSSIBLE")
  exit()
s = mgcd(a)
if s==1:
  print('POSSIBLE')
else:
  if k%s==0:
    print("POSSIBLE")
  else:
    print("IMPOSSIBLE")