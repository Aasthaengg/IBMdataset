#D問題
import heapq
N = int(input())
AB = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    AB[a].append(b)
    AB[b].append(a)
    
C = list(map(int,input().split()))
C.sort(reverse=True)

var = [0 for i in range(N)]
var[0] = C[0]
Q = []
heapq.heappush(Q,0)
ind = 1

for i in range(N-1):
    q = heapq.heappop(Q)
    for j in AB[q]:
        if var[j] == 0:
            var[j] = C[ind]
            ind+=1
            heapq.heappush(Q,j)
            
print(sum(C)-C[0])
for v in var:
    print(v,end=" ")
