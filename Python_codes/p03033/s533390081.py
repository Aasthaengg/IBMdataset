import sys
from bisect import *

input = sys.stdin.readline

def f(n, q):
    xst = []
    for i in range(n):
        s, t, x = map(int, input().split())
        xst.append([x, s - x, t - x])
    xst.sort()

    ds = []
    for i in range(q):
        d = int(input())
        ds.append(d)

    ans = [-1] * q
    jump = [-1] * q

    for x, s, t in xst:
        i = bisect_left(ds, s)
        fi = bisect_left(ds, t)
        while i < fi:
            if jump[i] != -1:
                i = jump[i]
            else:
                ans[i] = x
                jump[i] = fi
                i += 1

    print(*ans, sep="\n")

n, q = map(int, input().split())
f(n, q)
