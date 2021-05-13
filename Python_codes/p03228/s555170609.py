#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cookie(p1,p2):
	if p1 % 2 == 1:
		p1 -= 1
	p1 /= 2
	p2 += p1
	return p1,p2

a,b,k = map(int, input().split())
for i in range(k):
	if i % 2 == 0:
		a,b = cookie(a,b)
	else:
		b,a = cookie(b,a)
print("{} {}".format(int(a),int(b)))
