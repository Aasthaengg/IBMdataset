# coding: utf-8
import sys

line = sys.stdin

count = 1
for x in line :
	if int(x) == 0 :
		break
	print('Case {0}: {1}'.format(count, x), end='')
	count += 1