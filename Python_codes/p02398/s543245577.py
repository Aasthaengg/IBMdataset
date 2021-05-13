a,b,c = map(int, raw_input().split(" "))
result = 0
for v in xrange(a, b+1):
	if (c % v) == 0:
		result += 1
print result