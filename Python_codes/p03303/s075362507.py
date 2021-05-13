s = raw_input()
w = int(raw_input())

ss = ''

for i in xrange(0, len(s), +w): ss += s[i]

print ss
