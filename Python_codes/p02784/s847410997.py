import sys
from itertools import accumulate

H, N = map(int, next(sys.stdin.buffer).split())
A = map(int, next(sys.stdin.buffer).split())

ans = any(map(lambda v: v >= H, accumulate(A, initial=0)))

print('Yes' if ans else 'No')