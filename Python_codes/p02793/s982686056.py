from math import gcd
from functools import reduce

MOD = 10 ** 9 + 7

def calc_lcm(x, y):
    return x * y // gcd(x, y)

def calc_lcm_list(numbers):
    return reduce(calc_lcm, numbers, 1)
  
  
N, *A = map(int, open(0).read().split())
lcm = calc_lcm_list(A)
print(sum(lcm // v for v in A) % MOD)
