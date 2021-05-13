r,c=map(int,raw_input().split())
a=[map(int,raw_input().split()) for _ in xrange(r)]
sums,l=0,[]
for i in xrange(r):
	a[i].append(sum(a[i]))
for i in xrange(c+1):
	for j in xrange(r):
		sums+=a[j][i]
	l.append(sums)
	sums=0
a.append(l)
for i in a:
	for j in xrange(c+1):
		if j==c: print i[j]
		else: print i[j],