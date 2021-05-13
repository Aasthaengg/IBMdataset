import sys
sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def SMI(): return input().split()
def SLI(): return list(input())

def printlist(lst, k=' '): print(k.join(list(map(str, lst))))
INF = float('inf')

from math import ceil, floor, log2
# from collections import deque
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np
# from numpy import cumsum  # accumulate

from fractions import gcd
# from math import gcd
def lcm(x, y):
  return x // gcd(x, y) * y

def solve():
    N, M = MI()
    A = LI()

    A = list(map(lambda x: x // 2, A))

    EX = 0
    b = A[0]
    while b % 2 == 0:
        b //= 2
        EX += 1

    l = 1
    for a in A:
        ex = 0
        while a % 2 == 0:
            a //= 2
            ex += 1
        if ex != EX:
            print(0)
            return
        l = lcm(l, a)

    M //= pow(2, EX)
    # print(l)

    print(ceil((M // l) / 2))


if __name__ == '__main__':
    solve()
