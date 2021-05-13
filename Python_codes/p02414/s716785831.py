# -*- coding: utf-8 -*-
def makeEmptyMatrix(i, j):
	mat = [[]] * i
	for a in xrange(i):
		mat[a] = [0] * j
	return mat

n, m, l = map(int, raw_input().split())
A = makeEmptyMatrix(n, m)
B = makeEmptyMatrix(l, m)
for i in xrange(n):
 A[i] = map(int, raw_input().split())

for i in xrange(m):
 for j, v in enumerate(map(int, raw_input().split())):
  B[j][i] = v

for a in A:
 for b in B:
  ttl = 0
  for i, j in zip(a, b): ttl += i*j
  print ttl,
 print