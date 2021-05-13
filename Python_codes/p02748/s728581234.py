from collections import defaultdict
import numpy as np

A, B, M = map(int, input().split())
a = np.array(list(map(int, input().split())))
b = np.array(list(map(int, input().split())))

ans = a.min() + b.min()

for i in range(M):
    x, y, c = map(int, input().split())
    ans = min(ans, a[x-1] + b[y-1] - c)

print(ans)