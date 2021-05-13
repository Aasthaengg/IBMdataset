n,k=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in range(n):
    m[i]*=(-1)

import heapq
heapq.heapify(m)
for i in range(k):
    p=heapq.heappop(m)
    heapq.heappush(m,p/2)
s=0
for i in range(n):
    s+=int(abs(m[i]))
print(s)