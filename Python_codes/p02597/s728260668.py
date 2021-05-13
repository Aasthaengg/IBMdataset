#!/usr/bin/env python
# -*- coding: utf-8 -*-

input()
stones = input()
red_count = 0
for stone in stones:
	if stone == 'R':
		red_count += 1

white_count = 0
for stone in stones[:red_count]:
	if stone == 'W':
		white_count += 1

print(white_count)
