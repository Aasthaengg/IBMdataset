import collections
import heapq
n = int(raw_input())
ais = [0] + map(int, raw_input().split()) 
res = [0 for __ in range(n +1)]
used = set([])
for u in range(n, 0, -1):
	c = u*2
	cumul = 0
	for jj in range(u, n+1, u):
		cumul += res[jj]
	
	if ais[u] != (cumul % 2): 
		res[u] = 1
		used.add(u)
s = sum(res)
print s
if s:
	for x in used: print x,
	print