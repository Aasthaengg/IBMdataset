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
def MS(): return input().split()
def LS(): return list(input())
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def printlist(lst, k=' '): print(k.join(list(map(str, lst))))
INF = float('inf')
# from math import ceil, floor, log2
from collections import deque, defaultdict
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

from math import gcd

def solve():
    N = II()
    A = LI()
    
    mx = 1000003
    D = [1] * mx
    for i in range(2, len(D)):
        if D[i] != 1:
            continue
        for j in range(i, len(D), i):
            if D[j] == 1:
                D[j] = i

    # def fast_make_divisor(x):
    #     d = D[x]
    #     divisors = [d]
    #     while x != d:
    #         x = x // d
    #         d = D[x]
    #         divisors.append(d)
    # # print(divisors)
    #     return divisors

    g = A[0]
    dct = defaultdict(int)
    flag = True
    for a in A:
        g = gcd(g, a)
        # print(a, D[a])
        # if D[a] != 1:
        #     if dct[D[a]] > 0:
        #         flag = False
        #     dct[D[a]] += 1
        # print(a, fast_make_divisor(a))
        d = D[a]
        p = a
        # 最小の素数を求める
        while p != d:
            p = p // d
            d = D[p]

        if p != 1:
            dct[p] += 1
            if dct[p] > 1:
                flag = False

    if g == 1:
        if flag:
            print('pairwise coprime')
        else:
            print('setwise coprime')
    else:
        print('not coprime')


if __name__ == '__main__':
    solve()

