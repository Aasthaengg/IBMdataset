R = [0 for i in xrange(0,200000)] 
n = int(raw_input())
for i in xrange(n):
	R[i] = int(input())
maxv = -2000000000
minv = R[0]
for j in xrange(1, n):
	maxv = max(maxv, R[j]-minv)
	minv = min(minv, R[j])
print maxv 