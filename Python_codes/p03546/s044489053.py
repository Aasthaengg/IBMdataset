#!/usr/bin/env python3
h, w = map(int, input().split())
c = [[*map(int, input().split())] for _ in range(10)]
a = [[*map(int, input().split())] for _ in range(h)]
d = [c[i][1] for i in range(10)]
for i in range(10):
    for j in range(10):
        d[j] = min(d[j], min(c[j][k] + d[k] for k in range(10)))
d += [0]
print(sum(d[i] for i in sum(a,[])))
