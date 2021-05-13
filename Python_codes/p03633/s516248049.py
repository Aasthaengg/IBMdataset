n=int(input())
t=[int(input()) for _ in range(n)]

from fractions import gcd
from functools import reduce
def lcm(x,y):return x*y//gcd(x,y)
ans=reduce(lcm,t)
print(ans)