
import collections
n,ais,cc = int(raw_input()), map(int, raw_input().split()), collections.Counter()
for ai in ais:
	if ai % 4 == 0: cc[0] += 1
	elif ai % 2 == 0: cc[1] += 1
	else: cc[2] += 1

p,h = 0, [[2,1,0],[1],[0]] 
while(n):
	for u in h[p] + [-1]:
		if u == -1: 
			p =-1
			break
		if cc[u] > 0:
			p = u
			cc[u] -=1
			n -=1
			break
	if p == -1: break

print 'Yes' if n == 0 else 'No'