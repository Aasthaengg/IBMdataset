#!/usr/bin/env python3
n, c, k = map(int, input().split())
a = sorted([int(input()) for i in range(n)])

ans = 0
busp = 0
machi = 0

for i in a:
    if busp == 0:
        busp += 1
        machi = i + k
        if busp >= c:
            ans += 1
            busp = 0
            machi = 0

    elif i <= machi:
        busp += 1
        if busp >= c:
            ans += 1
            busp = 0
            machi = 0

    elif i > machi:
        ans += 1
        busp = 1
        machi = i + k

if busp >= 1:
    ans += 1

print(ans)
