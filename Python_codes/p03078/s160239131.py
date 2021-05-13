#123_D
import heapq
ans = []
heapq.heapify(ans)
x, y, z, k = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse= True)
b = sorted(list(map(int, input().split())), reverse= True)
c = sorted(list(map(int, input().split())), reverse= True)

for i in range(x):
    p = k // (i+1)
    for j in range(min(p + 1, y)):
        q = p // (j+1)
        for l in range(min(q + 1, z)):
            heapq.heappush(ans, -(a[i] + b[j] + c[l]))
            
for _ in range(k):
    print(-heapq.heappop(ans))