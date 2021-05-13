#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))

ans = 1
f = 0

for i in range(n):
    if f == 0:
        f = 1
    elif f == 1:
        if a[i] > a[i - 1]:
            f = 2
        elif a[i] < a[i - 1]:
            f = 3
    elif f == 2:
        if a[i] < a[i - 1]:
            ans += 1
            f = 1
    elif f == 3:
        if a[i] > a[i - 1]:
            ans += 1
            f = 1
print(ans)
