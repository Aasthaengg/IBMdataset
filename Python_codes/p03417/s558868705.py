import itertools
import math
import sys
from collections import Counter
from fractions import gcd
from functools import reduce

n, m = map(int, input().split())
if n == m == 1:
    print(1)
elif n == 1:
    print(m - 2)
elif m == 1:
    print(n - 2)
else:
    print((n - 2) * (m - 2))
