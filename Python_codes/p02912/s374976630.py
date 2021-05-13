import heapq
n,m=map(int,input().split())
alist=list(map(int,input().split()))
malist=[]
for a in alist:
    malist.append(-a)

heapq.heapify(malist)

for i in range(m):
    tmp = -heapq.heappop(malist)
    tmp //= 2
    heapq.heappush(malist,-tmp)

print(-sum(malist))
