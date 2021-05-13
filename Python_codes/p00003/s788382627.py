# -*- coding: utf-8 -*-

import sys
import os

N = int(input())
for i in range(N):
    lst = list(map(int, input().split()))
    mx = max(lst)
    lst.remove(mx)

    if mx * mx == lst[0] * lst[0] + lst[1] * lst[1]:
        print('YES')
    else:
        print('NO')