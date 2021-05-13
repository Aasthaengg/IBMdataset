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
# from collections import deque
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np
# from numpy import cumsum  # accumulate

def solve():
    N, P = MI()
    A = LI()

    odd = 0
    even = 0
    for a in A:
        if a % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 0:
        # 全て偶数
        if P == 0:
            print(pow(2, even))
        else:
            print(0)
    else:
        # 奇数が存在する
        # 一つの奇数に着目すると、それ以外の数の合計が奇数か偶数になるかによって
        # 選ぶ選ばないを選択することでPにすることができる
        print(pow(2, N-1))

if __name__ == '__main__':
    solve()
