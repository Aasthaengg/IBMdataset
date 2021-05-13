# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
if N == 1:
    print('Hello World'); exit()
A = ir(); B = ir()
answer = A + B
print(answer)
