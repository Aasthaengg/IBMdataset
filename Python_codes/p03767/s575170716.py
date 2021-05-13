#!/usr/bin/env python3
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

ans = 0

for i in range(1, len(a), 2):
    if i >= n * 2:
        break
    ans += a[i]

print(ans)