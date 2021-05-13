#!/usr/bin/env python3
a, b = map(int, input().split())

ans = 0

for i in range(a, b + 1):
    k = str(i)
    gk = k[::-1]

    if k == gk:
        ans += 1

print(ans)
