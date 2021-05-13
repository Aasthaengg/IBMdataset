# GCD and LCM

import sys


def gcd(x, y):
	while x != y:
		if x > y:
			x -= y
		else:
			y -= x
	return x

datas = []

for line in sys.stdin:
	datas.append(map(int, line.split()))

for data in datas:
	g = gcd(data[0], data[1])
	print "{0} {1}".format(g, data[0] * data[1] / g)