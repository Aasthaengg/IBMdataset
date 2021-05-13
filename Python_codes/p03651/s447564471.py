#! /usr/bin/env python3

import sys
import math
from functools import reduce
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)


def gcd(numbers):
    return reduce(math.gcd, numbers)


N, K, *A = map(int, read().split())

G = gcd(A)

if (K % G == 0) & (K <= max(A)):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
