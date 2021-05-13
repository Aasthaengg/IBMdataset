import numpy as np
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())

edge = np.zeros(n, dtype=int)
for _ in range(m):
    a, b = map(int, readline().split())
    edge[a - 1] += 1
    edge[b - 1] -= 1

np.add.accumulate(edge, out=edge)
if all(edge % 2 == 0):
    ans = "YES"
else:
    ans = "NO"

print(ans)
