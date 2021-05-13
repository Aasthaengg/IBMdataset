import itertools
import math
import sys
from collections import Counter
from fractions import gcd
from functools import reduce

n, m = map(int, input().split())
print((100 * (n - m) + 1900 * m) * 2 ** m)
