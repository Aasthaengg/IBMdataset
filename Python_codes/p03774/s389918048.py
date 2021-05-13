#!/usr/bin/env python3
N, M = map(int, input().split())
a = [0] * N
b = [0] * N
for i in range(N):
    a[i], b[i] = map(int, input().split())
c = [0] * M
d = [0] * M
for i in range(M):
    c[i], d[i] = map(int, input().split())

for i in range(N):
    x = 0
    y = 0
    dist = 10**20
    ans = 0
    for j in range(M):
        x = abs(a[i] - c[j])
        y = abs(b[i] - d[j])
        if x + y < dist:
            dist = x + y
            ans = j + 1
    print(ans)
