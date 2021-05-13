#!/usr/bin/env python3

N, T = map(int, input().split())

ans = 10**9
for i in range(N):
    c, t = map(int, input().split())
    if t <= T and ans > c:
        ans = c

if ans == 10**9:
    print('TLE')
else:
    print(ans)

