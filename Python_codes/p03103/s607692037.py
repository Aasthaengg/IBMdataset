#!/usr/bin/env python3
n, m = map(int, input().split())
v = []
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    v += [(a, b)]
v.sort(key=lambda x: x[0])
for i in v:
    m -= i[1]
    if m >= 0:
        ans += i[0]*i[1]
    else:
        m += i[1]
        ans += m*i[0]
        break
print(ans)
