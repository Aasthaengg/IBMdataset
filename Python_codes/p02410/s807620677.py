n, m = map(int, raw_input().split())
A = [map(int, raw_input().split()) for i in xrange(n)]
B = [int(raw_input()) for i in xrange(m)]
for i in xrange(n):
    print sum(A[i][j] * B[j] for j in xrange(m))