# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

H, W = lr()
h, w = lr()
answer = (H-h) * (W-w)
print(answer)
