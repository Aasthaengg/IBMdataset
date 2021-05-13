import numpy as np
import sys
input = sys.stdin.buffer.readline

def baku(x):
    g = h - b*x
    g = g[g>0]
    g += a-b-1
    g //= a-b
    if sum(g) <= x:
        return True
    else:
        return False

n, a, b = map(int,input().split())
h = []
for i in range(n):
    h.append(int(input()))
h = np.array(h, dtype=np.int64)

lb = 0
ub = 10**9 + 1
while ub - lb > 1:
    x = (ub+lb) //2
    if baku(x):
        ub = x
    else:
        lb = x
print(ub)