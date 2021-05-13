from fractions import gcd
from functools import reduce
from math import ceil

n, m = map(int, input().split())
a = list(map(int, input().split()))

b = list(map(lambda x: format(x, 'b')[::-1].find('1'), a))
if len(set(b)) != 1:
    print(0)
else:
    c = list(map(lambda x: x//2, a))
    t = reduce(lambda x, y: x*y//gcd(x, y), c)
    print(ceil((m//t)/2))
