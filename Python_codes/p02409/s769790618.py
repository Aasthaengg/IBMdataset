BLD = [[[0 for k in xrange(10)] for i in xrange(3)] for j in xrange(4)]

for i in xrange(input()):
    b, f, r, v = map(int, raw_input().split())
    BLD[b-1][f-1][r-1] += v

for b in xrange(4):
    for f in xrange(3):
        print ' ' + ' '.join(map(str, BLD[b][f]))
    if b != 3:
        print '####################'