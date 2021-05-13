# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

L = ir()
answer = L ** 3 / 27
print(answer)
