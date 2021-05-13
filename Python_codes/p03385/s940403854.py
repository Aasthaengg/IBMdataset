# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

S = sr()
kind = len(set(S))
bl = kind == 3
print('Yes' if bl else 'No')
