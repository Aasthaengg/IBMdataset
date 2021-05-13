(n, m) = map(int, raw_input().split())

A = []
for i in xrange(0,n):
	line = map(int, raw_input().split())
	A.append(line)

b = []
for j in xrange(0,m):
	temp = int(raw_input())
	b.append(temp)

result = []
for x in xrange(0,n):
	temp = 0
	for y in xrange(0,m):
		temp = temp + A[x][y] * b[y]
	result.append(temp)

for k in xrange(0,n):
	print result[k]