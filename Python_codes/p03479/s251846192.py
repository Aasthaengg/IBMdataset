# -*- coding: utf-8 -*-
X, Y = map(int, input().split(' '))
ans = 0
n = X
while n <= Y:
    ans += 1
    n *= 2

print(ans)
