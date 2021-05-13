# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

A = ir()
B = ir()
C = ir()
D = ir()
answer = min(A, B) + min(C, D)
print(answer)
