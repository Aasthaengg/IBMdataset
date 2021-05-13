#!/usr/bin/env python3
n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
d.sort()
t.sort()

idx_d, idx_t = 0, 0
while idx_t < m and idx_d < n:
    if d[idx_d] == t[idx_t]:
        idx_d += 1
        idx_t += 1
    elif d[idx_d] > t[idx_t]:
        print("NO")
        exit()
    else:
        idx_d += 1
if idx_t < m - 1:
    print("NO")
else:
    print("YES")
