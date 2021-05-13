from fractions import gcd
from functools import reduce
#from collections import deque
# from math import factorial
# import collections
import sys
sys.setrecursionlimit(2000000)
# import itertools
# import statistics
# import numpy as np
n = input()
#n, m = list(map(int, input().split()))
a = list(map(int, input().split()))


def lcm_base(x, y):
    return (x * y) // gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


b = lcm_list(a)-1
f = 0
for i in a:
    f += b % i

print(f)
