
import collections
n,m = map(int,raw_input().split(' '))

costs = [map(int, raw_input().split(' ')) for _ in range(n)]
costs.sort(key = lambda x:-x[0])
q = collections.deque(costs)
r = 0
while(m):
	u,v = q.pop()
	t = min(v,m)
	m -=t
	r += t * u
print r