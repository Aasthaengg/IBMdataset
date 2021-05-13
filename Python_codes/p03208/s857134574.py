#!/usr/bin/env python3
n, k, *h = map(int, open(0).read().split())
h.sort()
ans = []
for i in range(n-k+1):
    ans += [h[k+i-1] - h[i]]
print(min(ans))
