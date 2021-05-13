
import collections
n = int(raw_input())
cca = collections.Counter([raw_input() for _ in range(n)])
m = int(raw_input())
ccb = collections.Counter([raw_input() for _ in range(m)])

r = 0
for w in cca.keys() + ccb.keys():
	r = max(r,cca[w] - ccb[w])
print r