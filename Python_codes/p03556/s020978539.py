# -*- coding: utf-8 -*-

N = int(input())

ans = 1
i = 1

while True:
    ans = i ** 2
    i += 1
    if i ** 2 > N:
        break

print(ans)