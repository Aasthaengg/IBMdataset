# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
time = N // 7
bl = False

for x in range(time+1):
    y = N - x * 7
    if y % 4 == 0:
        bl = True; break

print('Yes' if bl else 'No')
