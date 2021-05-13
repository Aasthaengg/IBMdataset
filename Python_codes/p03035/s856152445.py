# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

A, B = lr()
answer = B if A >= 13 else B // 2 if A >= 6 else 0
print(answer)
# 40