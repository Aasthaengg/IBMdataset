k,t = map(int,input().split())
a = sorted(list(map(int,input().split())),reverse=True)
for i in range(t):
    a[i] = -a[i]
import heapq
heapq.heapify(a)
buf = heapq.heappop(a)+1
while len(a)>0:
    x = heapq.heappop(a)
    if buf!=0:
        heapq.heappush(a,buf)
    buf = x+1
print(-buf)