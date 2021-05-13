#!/usr/bin/env python

from collections import deque
import itertools as ite
import sys
import math

sys.setrecursionlimit(1000000)

INF = 10 ** 18
MOD = 10 ** 9 + 7

S = raw_input()
if S.count("x") <= 7:
    print "YES"
else:
    print "NO"