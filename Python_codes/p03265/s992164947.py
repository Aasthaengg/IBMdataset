import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

x1, y1, x2, y2 = rm()
c1, c2 = x1+y1*1j, x2+y2*1j
c3, c4 = -1j*(c1-c2) + c2, 1j*(c2-c1) + c1
print(int(c3.real), int(c3.imag), int(c4.real), int(c4.imag))


