# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

A = np.array(lr())
bl = np.all(A <= 8)
print('Yay!' if bl else ':(')
