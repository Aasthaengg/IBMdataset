n,ais = int(raw_input()), map(int, raw_input().split())
import collections
cc = collections.Counter()
for ai in ais:
	if ai % 4 == 0: cc[0] += 1
	elif ai % 2 == 0: cc[1] += 1
	else: cc[2] += 1

q = collections.deque()
while(n):
	if len(q) == 0:
		for u in range(3)[::-1]:
			if cc[u] > 0:
				q.append(u)
				cc[u]-=1
				n -=1
				break
		if len(q) == 0: break
	else:
		if q[-1] == 0:
			if cc[2]:
				q.append(2)
				cc[2]-=1
				n-=1
			elif cc[1]:
				q.append(1)
				cc[1]-=1
				n-=1
			elif cc[0]:
				q.append(0)
				cc[0]-=1
				n-=1
			else:
				break
		elif q[-1] == 2:
			if cc[0] == 0:
				break
			else:
				q.append(0)
				cc[0]-=1
				n-=1
		elif q[-1] == 1:
			if cc[1] > 0:
				q.append(1)
				cc[1]-=1
				n-=1
			else:
				break

print 'Yes' if n == 0 else 'No'
