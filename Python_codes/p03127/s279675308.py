from math import gcd
from functools import reduce

input()
a = list(map(int, input().split()))
print(reduce(gcd, a))