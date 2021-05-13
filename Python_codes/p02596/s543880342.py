#!/usr/bin/env python
# -*- coding: utf-8 -*-

k = int(input())

n = 0
for i in range(1, k + 1):
	n = (10 * n + 7) % k
	if n == 0:
		print(i)
		break
else:
	print(-1)
