import sys
a = map(int, raw_input().split())
while a != [0,0]:
	for i in xrange(a[0]):
		for j in xrange(a[1]):
			if (i + j) % 2:
				sys.stdout.write('.')
			else:
				sys.stdout.write('#')
		print ""
	a = map(int, raw_input().split())
	print ""