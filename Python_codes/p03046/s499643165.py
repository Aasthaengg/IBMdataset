#!/usr/bin/env python3
m, k = map(int, input().split())

if 2**m - 1 < k:
    print(-1)
    exit()

if m == 1:
    if k == 0:
        print('0 0 1 1')
    else:
        print(-1)
    exit()

ans = [k]
left = []
for i in range(2**m):
    if i == k:
        continue
    left.append(i)
right = left[::-1]
ans = left + ans + right + ans
print(*ans)
