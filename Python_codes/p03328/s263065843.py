# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

A, B = lr()
diff = B - A
x = diff - 1
answer = x * (x+1) // 2 - A
print(answer)
