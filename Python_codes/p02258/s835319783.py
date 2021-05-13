# -*- coding: utf-8 -*-

if __name__ == '__main__':
	n = input()
	R = []

	for i in xrange(n):
		R.append(input())
	maxv = -20000000000
	minv = R[0]

	for i in xrange(1, n):
		maxv = max(maxv, R[i] - minv)
		minv = min(minv, R[i])

	print maxv