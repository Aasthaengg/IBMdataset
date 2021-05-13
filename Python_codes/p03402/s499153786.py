# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 上半分と下半分に分けて、１マスずつ塗っていく
A, B = lr()
X = [['#'] * 100 for _ in range(50)] + [['.'] * 100 for _ in range(50)]
A -= 1; B -= 1
h = 0; w = 0
while A:
    X[h][w] = '.'
    w += 2
    A -= 1
    if w >= 100:
        h += 2
        w = 0

h = 51; w = 0
while B:
    X[h][w] = '#'
    w += 2
    B -= 1
    if w >= 100:
        h += 2
        w = 0

X = [''.join(y) for y in X]
print(100, 100)
print('\n'.join(X))
