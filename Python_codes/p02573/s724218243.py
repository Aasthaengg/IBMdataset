import sys
import re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
# input = sys.stdin.readline
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

class UnionFind:

    def __init__(self,n):
        self.n = n
        self.root=[-1]*(n+1)
        self.rank=[0]*(n+1)

    def findRoot(self,x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.findRoot(self.root[x])
            return self.root[x]

    def unite(self,x,y):
        x=self.findRoot(x)
        y=self.findRoot(y)
        if x==y:
            return
        if self.rank[x] > self.rank[y]:
            self.root[x]+=self.root[y]
            self.root[y]=x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def isSameGroup(self,x,y):
        return self.findRoot(x)==self.findRoot(y)

    def count(self,x):
        return -self.root[self.findRoot(x)]


def main():
    N,M=i_map()
    A = []
    B=[]

    for i in range(0,M):
        tmp1,tmp2 = i_map()
        A.append(tmp1-1)
        B.append(tmp2-1)

    u = UnionFind(N)

    for i in range(0,M):
        u.unite(A[i],B[i])

    max = 0
    for i in range(0,N):
        if(max<=u.count(i)):
            max = u.count(i)

    print(max)

    return

if __name__ == '__main__':
    main()