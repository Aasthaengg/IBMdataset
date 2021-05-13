import heapq as hp
n,m=map(int,input().split())
a=[-int(x) for x in input().rstrip().split()]

hp.heapify(a)
for i in range(m):
    
    now=hp.heappop(a)
    now=-now//2
    hp.heappush(a,-now)

print(-sum(a))