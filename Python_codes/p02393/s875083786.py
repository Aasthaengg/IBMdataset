#!/usr/bin/env python
# -*- coding: utf-8 -*-

var = raw_input().split()

var = map(int, var)

if var[0] > var[1]:
	tmp = var[0]
	var[0] = var[1]
	var[1] = tmp
	
if var[0] > var[2]:
	tmp = var[0]
	var[0] = var[2]
	var[2] = tmp
	
if var[1] > var[2]:
	tmp = var[1]
	var[1] = var[2]
	var[2] = tmp

print var[0],var[1],var[2]