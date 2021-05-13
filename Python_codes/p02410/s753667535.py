n, m = map(int, raw_input().split())
A = [None] * n
for i in xrange(n):
    A[i] = map(int, raw_input().split())
b = [None] * m
for j in xrange(m):
    b[j] = input()

for i in xrange(n):
    k = 0
    for j in xrange(m):
        k += A[i][j] * b[j]
    print k