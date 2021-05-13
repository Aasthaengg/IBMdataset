# coding: utf-8
import sys
from itertools import product

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M = lr()
XYZ = [lr() for _ in range(N)]
answer = 0
for a, b, c in product([-1, 1], repeat=3):
    cand = list(x*a + y*b + z*c for x, y, z in XYZ)
    cand.sort(reverse=True)    
    temp = sum(cand[:M])
    if temp > answer:
        answer = temp

print(answer)
