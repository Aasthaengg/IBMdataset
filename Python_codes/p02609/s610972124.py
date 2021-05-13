import sys
# import math
# import bisect
# import numpy as np
# from decimal import Decimal
# from numba import njit, i8, u1, b1 #JIT compiler
# from itertools import combinations, product
# from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846

def read_str():      return sys.stdin.readline().strip()
def read_int():      return int(sys.stdin.readline().strip())
def read_ints():     return map(int, sys.stdin.readline().strip().split())
def read_ints2(x):   return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def GCD(a: int, b: int) -> int: return b if a%b==0 else GCD(b, a%b)
def LCM(a: int, b: int) -> int: return (a * b) // GCD(a, b)

def popcount(num):
    cnt = 0
    while num > 0:
        num %= bin(num).count('1')
        cnt += 1
    return cnt

def Main():
    n = read_int()
    x = read_str()
    x_int = int(x, 2)

    cnt = x.count('1')
    minus_cnt = cnt - 1
    plus_cnt = cnt + 1
    
    minus_mod = x_int % minus_cnt if minus_cnt != 0 else 0
    plus_mod = x_int % plus_cnt

    for i in range(n):
        if x[i] == '0':
            print(popcount((plus_mod + pow(2, n - 1 - i, plus_cnt)) % plus_cnt) + 1)
        elif minus_cnt != 0:
            print(popcount((minus_mod - pow(2, n - 1 - i, minus_cnt)) % minus_cnt) + 1)
        else:
            print(0)

if __name__ == '__main__':
    Main()