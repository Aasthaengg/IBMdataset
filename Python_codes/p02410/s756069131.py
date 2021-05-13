n,m = map(int,raw_input().split())
matrix = [[0 for x in xrange(m)] for y in xrange(n)]
vector = [0 for x in xrange(m)]
for x in xrange(n):
    matrix[x] = map(int,raw_input().split())
for x in xrange(m):
    vector[x] = input()
for x in xrange(n):
    ans = 0
    for y in xrange(m):
        ans += matrix[x][y]*vector[y]
    print ans