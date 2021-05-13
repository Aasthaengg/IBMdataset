from fractions import gcd
from functools import reduce


input()
A = map(int, input().split())
print(reduce(gcd, A))
