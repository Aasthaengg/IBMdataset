a = "CODEFESTIVAL2016"
b = raw_input()
r = 0
for i in xrange(len(a)):
	if a[i] != b[i]:
		r += 1
print r
