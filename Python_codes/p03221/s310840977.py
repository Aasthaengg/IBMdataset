
import collections
n,m = map(int, raw_input().split())
cities = [map(int,raw_input().split(' ')) + [i] for i in range(m)]
cities.sort(key  = lambda x :x[1] )
h = {}
def fill(s):
	return (max(0,6 - len(str(s))) * '0') + str(s)

cc = collections.Counter()
for p,y,i in cities:
	cc[p] += 1
	h[i] = '{}{}'.format(fill(p),fill(cc[p]))

for i in range(m):
	print h[i]