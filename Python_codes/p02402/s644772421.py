# -*- coding: utf-8 -*-

import math

# ??\???
n = int(input())
a = []
for i in input().split():
    a.append(int(i))

a.sort()

print(a[0], a[n - 1], sum(a))