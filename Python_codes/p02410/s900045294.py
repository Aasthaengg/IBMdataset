n, m = map(int, raw_input().split())

A = [[0 for j in xrange(m)] for i in xrange(n)]

B = [0 for i in xrange(m)]

for i in xrange(n):
    tmp = map(int, raw_input().split())
    for j in xrange(m):
        A[i][j] = tmp[j]
        
for i in xrange(m):
    B[i] = input()

for i in xrange(n):
    tmp = 0
    for j in xrange(m):
        tmp += A[i][j] * B[j]
    print tmp