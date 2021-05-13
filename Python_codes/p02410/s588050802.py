n, m = map(int, raw_input().split())
 
a = [[0]*m for i in xrange(n)]
 
b = [0]*m
 
for i in xrange(n):
    tmp = map(int, raw_input().split())
    for j in xrange(m):
        a[i][j] = tmp[j]
for i in xrange(m):
    b[i] = input()
for i in xrange(n):
    tmp = 0
    for j in xrange(m):
        tmp += a[i][j] * b[j]
    print tmp