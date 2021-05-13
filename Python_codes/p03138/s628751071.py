import collections
import math
n,k = map(int, raw_input().split(' '))
ais = map(int, raw_input().split(' '))
r = 0
m = 42
x = 0
for ii in range(m, -1, -1):
	cc = collections.Counter([(ai >> ii) & 1 for ai in ais])
	if (x + (1 << ii) <= k):
		if cc[0] > cc[1]: x += (1 << ii)
		
	  
for ai in ais:
	r += ai ^ x
print r