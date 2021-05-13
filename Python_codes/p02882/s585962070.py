# https://atcoder.jp/contests/abc144/tasks/abc144_d

from math import pi, tan

a, b, x = map(int, input().split())
eps = 10e-8

def f(a, b, theta):
    if theta > pi / 2.0 - eps:
        return 0.0
    ret = 0.0
    if a * tan(theta) <= b:
        ret = a * a * b - a * a * a * tan(theta) / 2.0
    else:
        ret = b * b / tan(theta) * a / 2.0
    return ret

ng = 0.0
ok = pi / 2.0
for _ in range(100000):
    mid = (ok + ng) / 2.0
    if f(a, b, mid) < x:
        ok = mid
    else:
        ng = mid
print("{:.10f}".format(ok / pi * 180))