import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B, Q = mapint()
Ss = [-10**20]+[int(input()) for _ in range(A)]+[10**20]
Ts = [-10**20]+[int(input()) for _ in range(B)]+[10**20]
Ss.sort()
Ts.sort()
from bisect import bisect_left

for _ in range(Q):
    x = int(input())
    xs = bisect_left(Ss, x)
    xt = bisect_left(Ts, x)

    rr = max(Ss[xs]-x, Ts[xt]-x)
    ll = max(x-Ss[xs-1], x-Ts[xt-1])
    lr = min(abs(x-Ss[xs-1])*2+abs(x-Ts[xt]), abs(x-Ts[xt-1])*2+abs(x-Ss[xs]))
    rl = min(abs(x-Ss[xs-1])+abs(x-Ts[xt])*2, abs(x-Ts[xt-1])+abs(x-Ss[xs])*2)
    print(min(rr, ll, rl, lr))