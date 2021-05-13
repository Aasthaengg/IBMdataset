from operator import mul
from functools import reduce

def factorial(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

n, m = map(int, input().split())

if n < 2:
    ans_1 = 0
else:
    ans_1 = factorial(n, 2)
if m < 2:
    ans_2 = 0
else:
    ans_2 = factorial(m, 2)
print(ans_1+ans_2)