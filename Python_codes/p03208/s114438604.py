#!/usr/bin/env python3

n, k = map(int, input().split())
h = [0 for _ in range(n)]
for i in range(n):
    h[i] = int(input())

h = sorted(h)
ans = 1001001001
for i in range(n-k+1):
    ans = min(ans, h[i+k-1]-h[i])

print(ans)
