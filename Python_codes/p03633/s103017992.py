from fractions import gcd
from functools import reduce


N, *T = map(int, open(0).read().split())
print(reduce(lambda x, y: x * y // gcd(x, y), T))
