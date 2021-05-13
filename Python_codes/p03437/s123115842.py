#!/usr/bin/env python3
x, y = map(int, input().split())
for k in range(1, 100000):
    if k * x % y != 0:
        print(k * x)
        break
else:
    print(-1)
