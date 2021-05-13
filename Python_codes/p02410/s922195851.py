#-*- coding: utf-8 -*-

n, m = map(int, raw_input().split())
t = [0] * m
mx = t * n
for i in xrange(n):
	mx[i] = map(int, raw_input().split())

v = [0] * m
for i in xrange(m):
	v[i] = input()

for i in xrange(n):
	t = 0
	for j in xrange(m):
		t += mx[i][j] * v[j]
	print t