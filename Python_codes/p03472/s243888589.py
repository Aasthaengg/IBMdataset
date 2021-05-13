#!/usr/bin/env python3
import math

N, H = map(int, input().split())

data = []

for _ in range(N):
    a, b = map(int, input().split())
    data.append([a, True])
    data.append([b, False])

data = sorted(data)[::-1]
ans = 0

for d in data:
    flag = d[1]
    if flag:
        ans += math.ceil(H / d[0])
        break
    else:
        ans += 1
        H -= d[0]
        if H <= 0:
            break
    
print(ans)