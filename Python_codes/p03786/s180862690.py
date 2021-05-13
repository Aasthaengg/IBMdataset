#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
a.sort()
idx = 0
tmp = a[0]
for i in range(1, n):
    if tmp * 2 < a[i]:
        idx = i  # ここで併合できなくなり、i 以上しか無理になる
    tmp += a[i]
print(n - idx)

