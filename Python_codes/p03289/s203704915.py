import collections
r = raw_input()
print 'AC' if ( r[0] == 'A' and  collections.Counter(r[2:-1])['C'] == 1 and  all([l in set(['A', 'C']) or l.lower() ==l for l in r ])) else 'WA'