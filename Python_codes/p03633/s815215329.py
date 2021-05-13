n = int(input())
ab = [int(input()) for _ in range(n)] #数字1*複数列入力

import fractions
from functools import reduce
def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

print(lcm_list(ab))