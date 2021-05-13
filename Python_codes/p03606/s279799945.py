# -*- coding: utf-8 -*-
a = int(input())
e = 0
for i in range(a):
	b, c = map(int, input().split())
	d = c - b + 1
	e += d
print(e)