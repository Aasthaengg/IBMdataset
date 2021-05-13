n = int(raw_input())
R = [input() for i in range(n)]
maxv = -2000000000
minv = R[0]
for j in xrange(1, n):
	maxv = max(maxv, R[j]-minv)
	minv = min(minv, R[j])
print maxv 