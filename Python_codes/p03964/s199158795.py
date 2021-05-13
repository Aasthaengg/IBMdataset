import math
import numpy as np
from fractions import gcd
import fractions
import statistics
import collections
from functools import reduce
import itertools
from collections import defaultdict
import bisect
from fractions import Fraction
 
N = int(input())
ca, cb = 0, 0
for _ in range(N):
    a, b = map(int, input().split())
    if ca == 0 and cb == 0:
        ca, cb = a, b
    else:
        r = int(math.ceil(max(Fraction(ca, a), Fraction(cb,b))))
        ca, cb = a*r, b*r

print (ca + cb)