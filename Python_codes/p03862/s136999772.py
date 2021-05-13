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
	n, x = LI()
	a_list = LI()
	count = 0

	for i in range(n-1):
		a1, a2 = a_list[i], a_list[i+1]
		if a1 + a2 <= x:
			continue
		else:
			if a1 <= x:
				eat_candy = (a1+a2) - x
				a_list[i+1] -= eat_candy
				count += eat_candy
			else:
				a_list[i] = x
				a_list[i+1] = 0
				count += a1 + a2 - x

	print(count)


if __name__ == '__main__':
    main()