import sys
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip() # ignore trailing spaces

a,b = na()
if b%a == 0:
	print(a+b)
else:
	print(b-a)