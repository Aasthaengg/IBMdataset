#!/usr/bin/env python3
k, s = map(int, input().split())

ans = 0

for i in range(k + 1):
    for j in range(k + 1):
        a = s - i - j
        
        if a >= 0 and a <= k:
            ans += 1

print(ans)