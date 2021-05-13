import heapq
n,m = map(int,input().split())
a = [(-1)*int(i) for i in input().split()]
heapq.heapify(a)
while m >= 1:
	k = heapq.heappop(a)
	k *= -1
	k //= 2
	k *= -1
	heapq.heappush(a, k)
	m -= 1
print(-sum(a))