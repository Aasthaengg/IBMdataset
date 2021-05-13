import collections
cc = collections.Counter()
for l in raw_input():
	cc[l] +=1
	cc[l] %= 2
print 'Yes' if all([cc[k]%2==0 for k in cc]) else 'No'