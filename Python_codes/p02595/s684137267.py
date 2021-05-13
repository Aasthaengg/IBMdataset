#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

n, d = map(int, input().strip().split(' '))
count = 0
for i in range(n):
	x, y = map(int, input().strip().split(' '))
	if sqrt(x * x + y * y) <= d:
		count += 1

print(count)
