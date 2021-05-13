#!/usr/bin/env python3
a = int(input())#500y
b = int(input())#100y
c = int(input())#50y
x = int(input())

ans = 0

for i in range(a + 1):
    for j in range(b + 1):
        d = (x - (i * 500) - (j * 100)) // 50

        if d >= 0 and d <= c:
            ans += 1
print(ans)
