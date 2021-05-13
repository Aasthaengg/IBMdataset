from fractions import gcd
from functools import reduce
AB = list(map(int, input().split()))

def lcm_base(x,y):
    return (x*y)//gcd(x,y)

def lcm(a):
    return reduce(lcm_base,a,1)
print(lcm(AB))