import heapq
n = int(raw_input())
heap = [map(int, raw_input().split(' '))[::-1] for _ in range(n)]
heapq.heapify(heap)
def f(heap):
	t = 0
	while(heap):
		nd,d = heapq.heappop(heap)
		gap = nd - t - d
		if gap < 0:
			return False
		t += d
		
	return True
print 'Yes' if f(heap) else 'No'