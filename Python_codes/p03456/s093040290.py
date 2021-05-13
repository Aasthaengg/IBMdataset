# -*- coding: utf-8 -*-

a, b = map(str, input().split())
ab = int(a + b)

tmp = 0
i = 1

while tmp <= 100100:
    tmp = i ** 2
    if ab == tmp:
        print('Yes')
        exit()
    i += 1

print('No')