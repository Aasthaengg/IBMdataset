import numpy as np

N = int(input())
A = list(map(int, input().split()))

r = sum(A)
l = 0

ans = np.inf
for ai in A:
    l += ai
    r -= ai
    ans = min(np.abs(r-l), ans)

print(ans)