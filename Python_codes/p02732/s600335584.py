from collections import Counter
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, *a = map(int, read().split())

c = Counter(a)

d = dict(c)
sm = 0
for k, v in c.items():
    mx = (v * (v - 1)) // 2
    nx = ((v - 1) * (v - 2)) // 2
    sm += mx
    d[k] = nx - mx

for v in a:
    print(sm + d[v])
