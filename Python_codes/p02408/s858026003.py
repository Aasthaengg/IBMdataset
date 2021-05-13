n = input()
a = []
c = []
for i in ['S ','H ','C ','D ']:
	for j in map(str,xrange(1,14)):
		a.append(i+j)
for i in xrange(n):
	a.remove(raw_input())
for i in xrange(len(a)):
	print a[i]