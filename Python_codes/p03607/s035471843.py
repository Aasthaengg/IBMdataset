import collections
cc = collections.Counter()
for _ in range(int(raw_input())):
	v = int(raw_input())
	cc[v] += 1
	if cc[v] == 2:
		cc[v] = 0
s = 0
for k in cc:
	if cc[k] == 1:
		s +=1
print s