import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
# from collections import Counter,defaultdict,deque
# from itertools import permutations, combinations
# from heapq import heappop, heappush
# from fractions import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

n = inp()
s = input()

r = []
g = []
b = []
for i in range(n):
    if s[i] == "R":
        r.append(i)
    if s[i] == "G":
        g.append(i)
    if s[i] == "B":
        b.append(i)

ans = len(r)*len(g)*len(b)

for i in range(1,n):
    for j in range(n):
        k = j + 2 * i
        if k < n and s[j] != s[j + i] and s[j] != s[j + 2 * i] and s[j + i] != s[j + 2 * i]:
            ans -= 1

print(ans)