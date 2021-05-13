import itertools
import math
import fractions
import functools
n, r = map(int, input().split())
if n >= 10: print(r)
else: print(r + 1000 - 100*n)