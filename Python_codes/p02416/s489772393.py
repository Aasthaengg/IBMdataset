#!/usr/bin/env python
#coding: UTF-8
import sys

a = sys.stdin.readlines()

for j in a:
	b = []
	for i in j.rstrip('\n'):
		b.append(int(i))
	if sum(b) == 0:
		break
	else:
		print sum(b)