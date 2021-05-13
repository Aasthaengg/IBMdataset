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
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    N = II()
    A = []
    B = []
    BA = []
    cnt = 0
    for i in range(N):
        s = input()
        l = list(s)
        if l[0] == 'B' and l[-1] == 'A':
            BA.append(i)
        elif l[0] == 'B':
            B.append(i)
        elif l[-1] == 'A':
            A.append(i)
        cnt += s.count('AB')
    # print(A, B, BA, cnt)
    la = len(A)
    lb = len(B)
    lba = len(BA)

    if la > 0 and lb > 0:
        cnt += min(la, lb) + lba
    elif la == 0 and lb == 0:
        if lba > 1:
            cnt += lba - 1
    else:
        cnt += lba
    print(cnt)


if __name__ == '__main__':
    solve()
