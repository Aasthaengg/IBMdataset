import sys
input = sys.stdin.readline
from collections import defaultdict, Counter

N = int(input())
for h in range(1, 3501):
    for n in range(1, 3501):
        x = (4*h*n-N*n-N*h)
        if x == 0:
            continue
        w = int(N*n*h/x)
        if w < 1 or 3500 < w:
            continue
        if N*(w*n+h*w+h*n) == 4*h*n*w:
            print(h, n, w)
            exit()
