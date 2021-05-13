import sys

while 1:
	h, w = map(int, raw_input().split())
	if h == 0 & w == 0:
		break
	else:
		for i in xrange(h):
			for j in xrange(w):
				sys.stdout.write("#")
			print ""
	print ""