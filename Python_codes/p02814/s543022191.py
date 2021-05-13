import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def SI(): return input().split()

def printlist(lst, k='\n'): print(k.join(list(map(str, lst))))
INF = float('inf')

from math import ceil, floor, log2
from collections import deque
from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product
from heapq import heapify, heappop, heappush

from fractions import gcd
def lcm(x, y):
  return x // gcd(x, y) * y

def solve():
    n, m = MI()
    A = LI()

    # aを2で割る
    for i in range(n):
        a = A[i]
        A[i] = a // 2

    def f(x):
        res = 0
        while x % 2 == 0:
            x //= 2
            res += 1
        return res

    div2 = f(A[0])
    for i, a in enumerate(A):
        if div2 != f(a):
            print(0)
            return
        A[i] = a >> div2

    m = m >> div2
    # print(A, m)

    l = 1
    for a in A:
        l = lcm(l, a)

    # print(l)

    # l * odd <= m を数える
    ans = m // l - m // (2 * l)
    print(ans)




if __name__ == '__main__':
    solve()
