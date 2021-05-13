n = input()
a = set()

for x in xrange(n):
	(i, f) = map(str, raw_input().split())
	if i == "insert":
		a.add(f)
	else:
		if f in a:
			print "yes"
		else:
			print "no"