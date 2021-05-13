import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B, Q = mapint()
Ss = [-10**18]+[int(input()) for _ in range(A)]+[10**18]
Ts = [-10**18]+[int(input()) for _ in range(B)]+[10**18]
from bisect import bisect_left

for q in range(Q):
    x = int(input())
    ls = Ss[bisect_left(Ss, x)-1]
    lt = Ts[bisect_left(Ts, x)-1]
    rs = Ss[bisect_left(Ss, x)]
    rt = Ts[bisect_left(Ts, x)]
    print(min((rs-lt)+min(rs-x, x-lt), (rt-ls)+min(rt-x, x-ls), max(x-ls, x-lt), max(rs-x, rt-x)))