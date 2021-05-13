# -*- coding: utf-8 -*-
A, B, C = map(int, input().split(' '))
import math

if C - A - B > 0:
    if 4 * A * B < (C - A- B) ** 2:
        print('Yes')
        exit(0)

print(('No'))
