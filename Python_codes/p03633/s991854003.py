N = int(input())
T=[]
for n in range(N):
    T.append(int(input()))
from fractions import gcd
from functools import reduce

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)
print(lcm_list(T))
