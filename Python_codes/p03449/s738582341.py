#!/usr/bin/env python3

n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

ini = a1[0]+sum(a2)
ans = ini
for i in range(1, n):
    s = ini - a2[i-1] + a1[i]
    if s >= ans:
        ans = s
    ini = s

print(ans)