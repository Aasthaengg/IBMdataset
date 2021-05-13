from fractions import gcd
from functools import reduce
n=int(input())
lst=[int(input()) for i in range(n)]
def lcm(x,y):
  return (x*y//gcd(x,y))
temp=reduce(lcm, lst, 1)
print(temp)