#!/usr/bin/env python

from collections import deque
import itertools as ite
import sys
import math

sys.setrecursionlimit(1000000)

INF = 10 ** 18
MOD = 10 ** 9 + 7

N, K = map(int, raw_input().split())
if K == 1:
	print 0
else:
	print N - K