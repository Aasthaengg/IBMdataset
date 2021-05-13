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
# from collections import deque, defaultdict
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    N = II()
    A = LI()
    B = LI()

    a = sum(A)
    b = sum(B)
    t = b - a
    if t < 0:
        print('No')
        return 
    a_cnt = 0
    b_cnt = 0
    for i in range(N):
        a = A[i]
        b = B[i]
        if a > b:
            c = a - b
            b_cnt += c
        elif a < b:
            c = b - a
            if c % 2 == 0:
                a_cnt += (c // 2)
            else:
                a_cnt += (c // 2) + 1
                b_cnt += 1
    # print(a_cnt, b_cnt, t - a_cnt, t - b_cnt)
    a_left = t - a_cnt
    b_left = t - b_cnt
    if a_left >= 0 and b_left >= 0:
        if a_left * 2 == b_left:
            print('Yes')
    else:
        print('No')

                
            

if __name__ == '__main__':
    solve()

