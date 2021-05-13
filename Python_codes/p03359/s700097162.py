# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

a, b = lr()
answer = a - 1
if b >= a:
    answer += 1
print(answer)
