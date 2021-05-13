a, b = map(lambda x: int(x) - 1, raw_input().split())
x = [['.'] * 100 for _ in xrange(100)]
for i in xrange(50, 100):
    for j in xrange(100):
        x[i][j] = '#'
for i in xrange(0, 50, 2):
    if b:
        for j in xrange(0, 100, 2):
            if b:
                x[i][j] = '#'
                b -= 1
for i in xrange(99, 49, -2):
    if a:
        for j in xrange(0, 100, 2):
            if a:
                x[i][j] = '.'
                a -= 1
print '\n'.join(['100 100'] + [''.join(_) for _ in x])
