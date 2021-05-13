import sys

count = 0

array = raw_input().split(' ')

a = int(array[0])
b = int(array[1])
c = int(array[2])

if (a < 1 or a > 10000) or (b < 1 or b > 10000) or (c < 1 or c > 10000):
	sys.exit()

for x in xrange(a,b+1):
	if c % x == 0:
		count =  count + 1

print count