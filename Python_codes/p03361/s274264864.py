# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

H, W = lr()
S = np.array([list(sr()) for _ in range(H)])
black = S == '#'
is_ok = np.zeros_like(S, dtype=np.bool)
is_ok[1:, :] |= black[:-1, :]
is_ok[:-1, :] |= black[1:, :]
is_ok[:, 1:] |= black[:, :-1]
is_ok[:, :-1] |= black[:, 1:]
impossible = (black & (~is_ok)).any()
print('No' if impossible else 'Yes')
