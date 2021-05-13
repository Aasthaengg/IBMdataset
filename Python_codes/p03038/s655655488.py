import heapq
n,m = map(int, raw_input().split(' '))
ais = map(int, raw_input().split(' '))
ais.sort()
heap = []
for _ in range(m):
	u,v = map(int,raw_input().split(' ')) 
	heapq.heappush(heap, (-v,u))
res = 0
for j in range(n):
	
	if heap and -heap[0][0] > ais[j]:
		u,v = heapq.heappop(heap)
		v-=1
		res += -u
		if v >= 1: heapq.heappush(heap, (u,v))
	else:
		res += ais[j]
print res