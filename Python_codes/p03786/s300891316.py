#!/usr/bin/env python3
n,*a=map(int, open(0).read().split())
a.sort()
ans = 0
c  = 0
for i in range(n-1):
    c += a[i]
    if c*2 < a[i+1]:
        ans = 0
    else:
        ans += 1
print(ans + 1)
