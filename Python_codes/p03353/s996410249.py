import heapq
s = raw_input()
k = int(raw_input())

heap = [(s[i], i) for i in range(len(s))]
heapq.heapify(heap)
seen = set()
while(k and heap):
	t,ii = heapq.heappop(heap)
	if t not in seen:
		seen.add(t)
		k-=1
		if k == 0:
			print t
	if ii + 1 < len(s):
		heapq.heappush(heap, (t + s[ii+1], ii+1))
	
