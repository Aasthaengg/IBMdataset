# coding: utf-8

import sys
import copy

M, K = (int(x) for x in input().split())

if K >= 2 ** M:
	print("-1")
	sys.exit()

if M == 0:
	print("0 0")
	sys.exit()

if M == 1:
	if K == 0:
		print("0 0 1 1")
		sys.exit()
	else:
		print("-1")
		sys.exit()

b = [x for x in range(2 ** M) if x != K]
c = list(reversed(copy.copy(b)))

for x in b:
	print(x, end = " ")

print(str(K), end = " ")

for x in c:
	print(x, end = " ")

print(str(K))