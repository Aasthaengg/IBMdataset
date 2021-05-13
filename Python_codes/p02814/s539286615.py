from math import gcd
from functools import reduce

N, M, *A = map(int, open(0).read().split())

def lcm(x, y):
    return x * y // gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm, numbers, 1)

def even_count(n):
    res = 0
    while n % 2 == 0:
        res += 1
        n //= 2
    return res


x = [v // 2 for v in A]
if all(even_count(v) == even_count(x[0]) for v in x):
    num = lcm_list(x)
    print(-(-(M // num) // 2))
else:
    print(0)

