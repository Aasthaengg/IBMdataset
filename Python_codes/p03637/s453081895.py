
import collections
n,ais = int(raw_input()), map(int, raw_input().split())
cc = collections.Counter()
for ai in ais:
	if ai % 4 == 0: cc[0] += 1
	elif ai % 2 == 0: cc[1] += 1
	else: cc[2] += 1

q,h = collections.deque([0]), [[2,1,0],[1],[0]] 
while(n):
	b = False
	for u in h[q[-1]] + [-1]:
		if u == -1: b = True
		if cc[u] > 0:
			q.append(u)
			
			cc[u] -=1
			n -=1
			break
	if b: break

print 'Yes' if n == 0 else 'No'