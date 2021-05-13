import sys
for i,ws in enumerate(sys.stdin, 1):
    w = ws[:-1]
    if w =='0': break
    print 'Case %d: %s' % (i, w)