#!/usr/bin/env python3
n, m = map(int, input().split())
(*a, ) = map(int, input().split())
a.sort()
q = [[*map(int, input().split())] for _ in range(m)]
q.sort(key=lambda x: -x[1])
idx = 0
for b, c in q:
    for _ in range(b):
        if idx >= n or a[idx] >= c:
            print(sum(a))
            exit()
        a[idx] = c
        idx += 1
print(sum(a))
