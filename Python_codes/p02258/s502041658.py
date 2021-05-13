# -*- coding: utf-8 -*-

import sys
import os
import math


N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))

max_profit = lst[1] - lst[0]
min_value = min(lst[0], lst[1])

for i in range(2, N):
    price = lst[i]
    max_profit = max(max_profit, price - min_value)
    min_value = min(min_value, price)

print(max_profit)