n = input()
d_s = {}
d_h = {}
d_c = {}
d_d = {}
for x in map(str, xrange(1, 14)):
    d_s[x] = 0 
    d_h[x] = 0 
    d_c[x] = 0 
    d_d[x] = 0 
for x in xrange(1, n+1):
    line = raw_input().split()
    if line[0]=='S':
        d_s[line[1]] = 1
    elif line[0]=='H':
        d_h[line[1]] = 1
    elif line[0]=='C':
        d_c[line[1]] = 1
    else:
        d_d[line[1]] = 1
d_key = ['S', 'H', 'C', 'D']
d_all = {d_key[0]: d_s, d_key[1]: d_h, d_key[2]: d_c, d_key[3]: d_d} 
for shcd in d_key:
    for rank in xrange(1, 14):
        if d_all[shcd][str(rank)]==0:
            print '%s %s' % (shcd, rank)