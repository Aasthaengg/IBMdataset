import math
from functools import reduce

N = int(input())
S = [int(input()) for _ in range(N)]

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

print(lcm_list(S))