n,m=map(int,raw_input().split())
A,B=[],[]
c=0
A=[map(int,raw_input().split()) for _ in [0]*n]
B=[int(raw_input()) for _ in [0]*m]
for i in xrange(n):
	print sum([A[i][j]*B[j] for j in xrange(m)])