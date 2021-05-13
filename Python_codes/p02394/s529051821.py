#!/usr/bin/env python
# -*- coding: utf-8 -*-

var = raw_input().split()

var = map(int, var)

if 0 > var[2] - var[4] or 0 > var[3] - var[4]:
	print "No"
elif var[0] < var[2] + var[4] or var[1] < var[3] + var[4]:
	print "No"
else:
	print "Yes"