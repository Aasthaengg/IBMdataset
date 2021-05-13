# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

C = np.array([list(sr()) for _ in range(3)])
answer = np.diag(C)
print(''.join(answer.astype(str)))
