# -*- coding: utf-8 -*-

X = int(input())

ans = 1
b = 1
p = 2

while b ** 2 <= X:
    p = 2
    while b ** p <= X and p <= X:
        ans = max(ans, b ** p)
        p += 1
    b += 1

print(ans)