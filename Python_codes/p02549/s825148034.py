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

def Main():
    n, k = read_ints()
    mod = 998244353
    dp = [0] * (n + 1)
    dp[0] = 1
    s = 1
    query = [read_int_list() for _ in range(k)]
    
    for i in range(1, n + 1):
        s += dp[i]
        for l, r in query:
            if l + i <= n:
                dp[i + l] = (dp[i + l] + s) % mod
            if r + i + 1 <= n:
                dp[i + r + 1] = (dp[i + r + 1] - s) % mod
    print(dp[n])

if __name__ == '__main__':
    Main()