import math
from functools import reduce

n = int(input())
t = list(int(input()) for _ in range(n))

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


print(lcm_list(t))
