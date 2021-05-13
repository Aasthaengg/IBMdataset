import sys
import os
if sys.platform=="darwin":
	base = os.path.dirname(os.path.abspath(__file__))
	name = os.path.normpath(os.path.join(base, '../Documents/input.txt'))
	#print(name)
	sys.stdin = open(name)

a,b,c = map(int,input().split())

ans = 0

if a+b>=c:
	print(b+c)
	exit()

if a>=c:
	print(b+c)
	exit()

else:
	ans = ans + a
	c = c - a
	if c == b:
		ans = ans + 2*b
	elif c < b:
		ans = b + c
	else:
		ans = ans + 2*b + 1

print(ans)

