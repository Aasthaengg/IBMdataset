import sys
import itertools
# import numpy as np
import time
import math
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
 
from functools import reduce
# from math import *
from fractions import *
N, M = map(int, readline().split())
A = list(sorted(map(lambda x: int(x) // 2, readline().split())))
min_cm = reduce(lambda a, b: (a * b) // gcd(a, b), A)
 
# print(all(map(lambda x: (min_cm // x) % 2 == 1, A)))
if not all(map(lambda x: (min_cm // x) % 2 == 1, A)):
    print(0)
    exit(0)
if min_cm > M:
    print(0)
    exit(0)
ans = (M // min_cm + 1) // 2
print(ans)