#D
import heapq

n,m = map(int,input().split())
a = list(map(int,input().split()))
bc = []
for i in range(m):
    b,c = map(int,input().split())
    bc.append((b,c))
bc.sort(key=lambda x:-x[1])
heapq.heapify(a)
for i in range(m):
    b,c = bc[i][0],bc[i][1]
    for j in range(b):
        p = heapq.heappop(a)
        if c > p:
            heapq.heappush(a,c)
        else:
            heapq.heappush(a,p)
            break
            
            
print(sum(a))