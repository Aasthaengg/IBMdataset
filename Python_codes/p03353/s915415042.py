from heapq import heappush, heappop
s = input()
K = int(input())
N = len(s)
heap = []
cnt = 0
for i in range(N):
	for j in range(i+1, min(i+K+1, N+1)):
		heappush(heap, s[i:j])

l = list(set(heap))
l.sort()
print(l[K-1])