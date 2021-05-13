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
	n = I()
	a_list = LI()
	a_dict = list(Counter(a_list).items())
	a_dict.sort()
	ans = 1
	if n % 2 == 0:
		for i in range(len(a_dict)):
			diff, number = a_dict[i]
			if diff % 2 == 0:
				ans = 0
				break
			if diff != 2*i+1 or number != 2:
				ans = 0
				break
			ans *= 2
			ans %= MOD
	else:
		for i in range(len(a_dict)):
			diff, number = a_dict[i]
			if diff % 2 == 1 or (diff == 0 and number !=1):
				ans = 0
				break
			if diff != 2*i or (diff > 0 and number != 2):
				ans = 0
				break
			if diff != 0:
				ans *= 2
				ans %= MOD
	print(int(ans))


	


if __name__ == '__main__':
    main()