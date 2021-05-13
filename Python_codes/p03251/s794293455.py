# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M, X, Y = lr()
x = lr(); x.append(X)
x.sort()
y = lr(); y.append(Y)
y.sort()
bl = y[0] > x[-1]
print('No War' if bl else 'War')
