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

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


def main():
	n = I()
	divisors_dict = {}
	for i in range(2,n+1):
		tmp_divisors = factorization(i)
		for tmp_divisor, num in tmp_divisors:
			if tmp_divisor in divisors_dict:
				divisors_dict[tmp_divisor] += num
			else:
				divisors_dict[tmp_divisor] = num
	ans = 1
	for divisor_num in divisors_dict.values():
		ans *= (divisor_num + 1)
		ans %= MOD
	print(ans)



if __name__ == '__main__':
    main()