a, b = map(int, input().split())

import math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

print(lcm_base(a, b))