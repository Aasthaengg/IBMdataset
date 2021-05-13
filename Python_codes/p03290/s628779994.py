#!/usr/bin/env python3
import math

D, G = map(int, input().split())
data = []
for i in range(D):
    p, c = map(int, input().split())
    data.append([100 * (i + 1), p, c])
data = sorted(data)[::-1]

ans = float("inf")

for i in range(2 ** D):
    total = 0
    num = 0
    idx = []
    for k in range(D):
        if i >> k & 1 == 1:
            idx.append(k)
    
    for j in idx:
        d = data[j]
        total += d[0] * d[1] + d[2]
        num += d[1]
    
    if total >= G:
        ans = min(ans, num)
    else:
        for j in set(range(D)) - set(idx):
            d = data[j]
            if total + d[0] * (d[1] - 1) >= G:
                num += math.ceil((G - total) / d[0])
                ans = min(ans, num)
                continue
            else:
                total += + d[0] * (d[1] - 1)
                num += d[1] - 1
print(ans)