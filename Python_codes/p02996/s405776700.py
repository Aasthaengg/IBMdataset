import heapq
n = int(raw_input())
heap = [map(int, raw_input().split(' '))[::-1] for _ in range(n)]
heapq.heapify(heap)
#(deadline, duration)
def f(heap):
	t = 0
	while(heap):
		nd,d = heapq.heappop(heap)
		gap = nd - t 
		gap -= d
		t += d
		while(heap and heap[0][0] == nd):
			_,v = heapq.heappop(heap) 
			t += v
			gap -= v
		if gap < 0: return False
	return True
print 'Yes' if f(heap) else 'No'