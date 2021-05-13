a, b, c = map(int, raw_input().split(' '))
print len([x for x in xrange(a, b+1) if not(c%x)])