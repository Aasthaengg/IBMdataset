import heapq
n,m=map(int,input().split())
a=[-int(i)for i in input().split()]
heapq.heapify(a)
for i in range(m):
 p=heapq.heappop(a)
 p*=-1
 p//=2
 heapq.heappush(a,-p)
print(-sum(a))