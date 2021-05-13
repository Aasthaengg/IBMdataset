import heapq as hp

n,m=[int(x) for x in input().rstrip().split()]
a=[-int(x) for x in input().rstrip().split()]

hp.heapify(a)

for i in range(m):
  now=hp.heappop(a)
  hp.heappush(a,-(-now//2))
print(-sum(a))

