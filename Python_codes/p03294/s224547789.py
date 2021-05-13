n=int(input())
a=list(map(int,input().split()))

from fractions import gcd
from functools import reduce
def lcm(x,y):
  return x*y//gcd(x,y)

q=reduce(lcm,a)

ans=0
for i in a:
  ans+=(q-1)%i
print(ans)