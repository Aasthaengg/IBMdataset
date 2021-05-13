import collections
cc = collections.Counter()
for _ in range(3):
	u,v = map(int ,raw_input().split())
	cc[u]+=1
	cc[v]+=1
print 'YES' if sorted([cc[a] for a in [1,2,3,4]]) == [1,1,2,2] else 'NO'