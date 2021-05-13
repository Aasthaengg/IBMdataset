import sys
def call(n):	
	for i in xrange(1, n+1):
		if (i % 3) == 0:
			sys.stdout.write(" " + str(i))
		elif (i % 10) == 3:
			sys.stdout.write(" " + str(i))
		else:
			x = i
			x = x / 10
			while x > 0:
				if (x % 10) == 3:
					sys.stdout.write(" " + str(i))
					break
				x = x / 10
				
	print ""
	

n = int(raw_input())
call(n)