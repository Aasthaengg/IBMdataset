#!/usr/bin/env python3
k, n = map(int, input().split())
a = list(map(int, input().split()))

ans = k

for i in range(len(a)):
    if i == 0:
        r = a[-1] - a[i]
        l = a[i] + (k - a[i + 1])
    elif i == n - 1:
        r = (k - a[i]) + a[i - 1]
        l = a[i] - a[0]
    else:
        r = (a[n-1] - a[i]) + ((k - a[n-1]) + a[i - 1])
        l = (a[i] - a[0]) + ((k - a[i + 1]) + a[i - 1])
    
    ans = min(ans, r, l)

print(ans)