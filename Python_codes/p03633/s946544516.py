from fractions import gcd
from functools import reduce


def lcm(a, b):
    return a * b // gcd(a, b)


N = int(input())
T = [int(input()) for _ in range(N)]

print(reduce(lcm, T))
