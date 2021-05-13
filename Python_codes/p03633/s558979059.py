import math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

N = int(input())
time = []

for i in range(N):
    a = int(input())
    time.append(a)

print(lcm(*time))
