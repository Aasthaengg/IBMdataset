import sys

s = input().split(' ')
d, n = int(s[0]), int(s[1])

if (n % 100 != 0):
	print (n * (100 ** d))
else :
	print ((n + 1) * (100 ** d))