import sys
import numpy as np
import random
from decimal import Decimal
import itertools
import re
import bisect
from collections import deque, Counter
from functools import lru_cache

sys.setrecursionlimit(10**9)
INF = 10**13
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
def SERIES(n): return np.fromstring(sys.stdin.buffer.read(), dtype=np.int32, sep=' ')
def GRID(h,w): return np.fromstring(sys.stdin.buffer.read(), dtype=np.int32, sep=' ').reshape(h,-1)[:,:w]
def GRIDfromString(h,w): return np.frombuffer(sys.stdin.buffer.read(), 'S1').reshape(h,-1)[:,:w]
MOD = 1000000007

def main():
	w, h, n = LI()
	left_x, right_x, lower_y, upper_y = 0, w, 0, h
	for _ in range(n):
		x, y, a = LI()
		if a == 1:
			left_x = max(x, left_x)
		elif a == 2:
			right_x = min(x, right_x)
		elif a == 3:
			lower_y = max(y, lower_y)
		elif a == 4:
			upper_y = min(y, upper_y)
	if right_x > left_x and upper_y > lower_y:
		print((right_x-left_x)*(upper_y-lower_y))
	else:
		print(0)


if __name__ == '__main__':
    main()