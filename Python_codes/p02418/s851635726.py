import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

if (p in s+s):
	print "Yes"
else:
	print "No"