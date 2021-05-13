#!/usr/bin/env python

from collections import deque, defaultdict
import itertools as ite
import sys
import math
from decimal import *

sys.setrecursionlimit(1000000)

INF = 10 ** 18
MOD = 10 ** 9 + 7

H = input()
W = input()
N = input()
den = max(H, W)
print N / den + (N % den != 0)