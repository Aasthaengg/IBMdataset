from functools import reduce
from fractions import gcd
def lcm(x,y):
  return x*y//gcd(x,y)
def lcmm(l):
  return reduce(lcm,l)
n=int(input())
t=[int(input()) for _  in range(n)]
print(lcmm(t))
