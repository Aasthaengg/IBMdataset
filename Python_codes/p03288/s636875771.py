# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

R = ir()
target = np.array([1200, 2800])
i = np.searchsorted(target, R, side='right')
answer = ['ABC', 'ARC', 'AGC'][i]
print(answer)
