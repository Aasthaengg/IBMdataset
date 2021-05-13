#!/usr/bin/env python3
n = int(input())
a = [0]
a += [int(input()) for i in range(n)]

cnt = 0
ps = 1

for _ in range(1, n + 1):
    ps = a[ps]
    cnt += 1

    if ps == 2:
        print(cnt)
        break
else:
    print(-1)
