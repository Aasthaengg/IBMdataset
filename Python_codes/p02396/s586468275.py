import sys
for i, line in enumerate(sys.stdin):
    x = int(line)
    if x == 0:
        break
    else:
        print 'Case %d: %d' % (i + 1, x)