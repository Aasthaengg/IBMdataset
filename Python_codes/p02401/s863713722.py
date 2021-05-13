# -*- coding: utf-8 -*-

import sys
import os
import math


for s in sys.stdin:
    lis = s.split()

    a = int(lis[0])
    op = lis[1]
    b = int(lis[2])

    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(math.floor(a / b))
    else:
        break