from math import gcd
from functools import reduce
f = lambda x,y: x*y//gcd(x,y)
print(reduce(f, [int(input()) for _ in range(int(input()))]))