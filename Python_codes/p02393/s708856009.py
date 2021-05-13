# -*- coding: utf-8 -*-

x = map(int, raw_input().split())

for e in sorted(x):
	if sorted(x).index(e) == len(x) - 1:
		print e
		break
	print e,