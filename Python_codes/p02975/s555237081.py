import collections as c
import sys

n = int(input())
a = list(map(int, input().split()))

A = c.Counter(a)

if list(A.keys()) == [0]:
	print("Yes")
	sys.exit()

if len(A.keys()) == 2:
	if 0 not in A.keys():
		print("No")
		sys.exit()
	else:
		if list(A.values())[0]*2 == list(A.values())[1]:
			print("Yes")
			sys.exit()
		else:
			print("No")
			sys.exit()

if len(A.keys()) != 3:
	print("No")
	sys.exit()

x,y,z = A.keys()
if x^y != z:
	print("No")
	sys.exit()

x,y,z = A.values()
if x == y == z:
	print("Yes")
else:
	print("No")