# -*- coding: utf-8 -*-

import sys
import os
import math


N = int(input())
cost = 100000

for i in range(N):
    cost *= 1.05
    cost = round(cost)

    if cost % 1000 > 0:
        cost = (cost // 1000) * 1000 + 1000
print(cost)