#!/usr/bin/env python
# -*- coding: utf-8 -*-

var = raw_input().split()

var = map(int, var)

if var[0] >= var[1]:
	print "No"
elif var[1] >= var[2]:
	print "No"
else:
	print "Yes"