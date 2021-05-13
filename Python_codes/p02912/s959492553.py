n,m = map(int,input().split())
a = list(map(int,input().split()))
import heapq
q = [0]*n
for i in range(n):
    q[i] = -a[i]
heapq.heapify(q) 
for i in range(m):
    x = heapq.heappop(q) 
    heapq.heappush(q,-(-x//2))
ans = 0
for i in range(n):
    x = heapq.heappop(q)
    ans += x
print(-ans)