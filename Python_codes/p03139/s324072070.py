#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(1000000)

INF = 10 ** 18

N, A, B = map(int, raw_input().split())

print min(A, B), max(0, A + B - N)