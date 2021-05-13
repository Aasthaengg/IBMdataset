import collections
cc = collections.Counter()
n,m = map(int, raw_input().split())
c = 0
r = 0


cc[c] += 1 

for ai in map(int, raw_input().split()):
	c += ai % m
	c %= m
	r += cc[c]
	cc[c] += 1
print r