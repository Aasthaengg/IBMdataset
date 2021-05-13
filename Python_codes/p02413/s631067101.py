# -*- coding: utf-8 -*-
r, c = map(int, raw_input().split())
cl= [0] * c
for i in xrange(r):
	t = map(int, raw_input().split())
	for i, a in enumerate(t):
		print a,
		cl[i] += a
	print sum(t)

for a in cl: print a,
print sum(cl)