#!/usr/bin/env python3
n, l = map(int, input().split())
ans = 10**9
for i in range(n):
    c, t = map(int, input().split())
    if t <= l:
        ans = min(ans, c)
if ans == 10**9:
    print('TLE')
else:
    print(ans)
