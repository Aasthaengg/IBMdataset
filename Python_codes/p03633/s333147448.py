N=int(input())
T_list=[int(input()) for _ in range(N)]

from functools import reduce
from fractions import gcd
def lcm(x,y):return x*y//gcd(x,y)
def lcmm(l):return reduce(lcm,l)
print(lcmm(T_list))