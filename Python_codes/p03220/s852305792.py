#!/usr/bin/env python3
n = int(input())
t,a = map(int,input().split())
h = list(map(int, input().split()))

ans = 0
ansc = 999999

for i in range(len(h)):
    c = abs(a - (t - h[i] * 0.006))
    if c < ansc:
        ansc = c
        ans = i + 1

print(ans)
