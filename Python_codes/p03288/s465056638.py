# coding: utf-8
import sys
from bisect import bisect_left, bisect_right

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

R = ir()
target = [1200, 2800]
i = bisect_right(target, R)
answer = ['ABC', 'ARC', 'AGC'][i]
print(answer)
