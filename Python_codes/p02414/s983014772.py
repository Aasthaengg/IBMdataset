n, m, l = map(int, raw_input().split())

A = [0]*n*m
for k in xrange(n):
    A[k*m:k*m+m] = map(int, raw_input().split())

B = [0]*m*l
for k in xrange(m):
    B[k*l:k*l+l] = map(int, raw_input().split())

C = [0]*n*l
for i in xrange(n):
    for j in xrange(l):
        for k in xrange(m):
            C[i*l + j] += A[i*m + k] * B[k*l + j]
        if j < l-1:
            print C[i*l + j],
        else:
            print C[i*l + j]