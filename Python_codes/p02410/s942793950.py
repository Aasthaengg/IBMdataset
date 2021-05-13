
m = map(int, raw_input().split())
a = [map(int, raw_input().split()) for i in xrange(m[0])]
b = [int(raw_input()) for i in xrange(m[1])]
for i in xrange(m[0]):
    print sum(a[i][j] * b[j] for j in xrange(m[1]))