import heapq
n = int(raw_input())
heap = [map(int, raw_input().split(' '))[::-1] for _ in range(n)]
heapq.heapify(heap)

def f(heap):
	t = 0
	while(heap):
		nd,ct = heapq.heappop(heap)
		while(heap and heap[0][0] == nd): ct += heapq.heappop(heap)[1]
		gap = nd - ct - t
		if gap < 0:
			return False
		while(heap and heap[0][1] <= gap):
			u,v = heapq.heappop(heap)
			gap -= v
			t += v
		t += ct
	return True
print 'Yes' if f(heap) else 'No'