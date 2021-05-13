import math
import heapq
n,m = map(int, raw_input().split(' '))

heap = [-e for  e in map(int, raw_input().split(' '))]
heapq.heapify(heap)
while(m and heap):
	u = heapq.heappop(heap)
	u *= -1
	u /=2
	if u:
		heapq.heappush(heap, -u)
	m-=1
	"""

	q = int(math.ceil(math.log(u,2)))
	if 2 ** q <= u: q +=1
	if q <= m:
		m-= q
	else:
		u /= 2
		m -=1
		if u:
			heapq.heappush(heap, -u)

	"""
print -sum(heap or [0])
