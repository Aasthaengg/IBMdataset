n = int(raw_input())
d = {}
for i in xrange(n):
    L = raw_input().split()
    if L[0] == 'insert':
        d[hash(L[1])] = L[1]
    else:
        if d.has_key(hash(L[1])):
            print 'yes'
        else:
            print 'no'