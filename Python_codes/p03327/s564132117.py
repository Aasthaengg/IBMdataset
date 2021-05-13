# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
answer = 'ABC' if N < 1000 else 'ABD'
print(answer)
