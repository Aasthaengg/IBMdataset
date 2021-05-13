import itertools
import math
import fractions
import functools

a, b = map(int, input().split())
print(a*b // fractions.gcd(a, b))