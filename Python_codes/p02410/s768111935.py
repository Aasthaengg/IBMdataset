n, m = map(int, raw_input().split())

a = [[0 for i in xrange(m)] for j in xrange(n)]
b = [0 for i in xrange(m)]

for i in xrange(n):
    tmp = map(int, raw_input().split())
    for j in xrange(m):
        a[i][j] = tmp[j]
for k in xrange(m):
    b[k] = int(raw_input())

for i in xrange(n):
    ans = 0
    for j in xrange(m):
        ans += a[i][j]*b[j]
    print ans