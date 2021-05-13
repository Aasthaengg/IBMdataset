#!/usr/bin/env python3
n = int(input())
k = len(str(n))
ans = 0
if k % 2 == 0:
    for i in range(k//2):
        ans += 10**((i*2)+1) - 10**(i*2)
else:
    for i in range(k//2):
        ans += 10**((i*2)+1) - 10**(i*2)
    ans += n - 10**(k-1) + 1
print(ans)
