import sys
import numpy as np


input = sys.stdin.readline
n, k, q = map(int, input().split())
l = np.zeros(n + 1)
d = {}

for _ in range(q):
    a = int(input())
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

for key, v in d.items():
    l[key] = v

l += k - q

for i in l[1:]:
    if i > 0:
        print("Yes")
    else:
        print("No")