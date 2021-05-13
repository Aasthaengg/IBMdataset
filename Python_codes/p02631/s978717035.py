from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter
from operator import mul
from functools import reduce

n = int(input())
a = list(map(int, input().split()))

m = a[0]
for i in range(1,n):
    m = m^a[i]

sol = [str(m^a[i]) for i in range(n)]
print(' '.join(sol))
