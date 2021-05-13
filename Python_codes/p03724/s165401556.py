import numpy as np
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = np.zeros(n + 1, dtype=int)
for _ in range(m):
    x, y = map(int, input().split())
    a[x] = (a[x] + 1) & 1
    a[y] = (a[y] + 1) & 1
print("YES" if np.sum(a) == 0 else "NO")
