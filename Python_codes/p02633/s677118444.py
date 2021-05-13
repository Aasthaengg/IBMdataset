# -*- coding: utf-8 -*-
x = int(input())
ans = x
ans2 = 0

print
for i in range(1, 1000):
    temp = ans * i
    if temp % 360 == 0:
        ans2 = i
        break

print(ans2)
