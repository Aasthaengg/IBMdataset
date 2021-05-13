#!/usr/bin/env python3
a, b, t = map(int, input().split())
tmp = a
ans = 0
while (True):
    for i in range(100):
        if a >= t + 0.5:
            print(ans)
            exit()
        a += tmp
        ans += b
