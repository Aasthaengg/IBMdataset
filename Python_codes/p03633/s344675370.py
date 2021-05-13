import math
from functools import reduce
N = int(input())
T = [int(input()) for _ in range(N)]

def lcm_b(x, y):
    return (x * y) // math.gcd(x, y)
def lcm(L):
    return reduce(lcm_b, L, 1)

print(lcm(T))