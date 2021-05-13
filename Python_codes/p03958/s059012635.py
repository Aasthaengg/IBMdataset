import heapq
K,T=map(int,input().split(' '))
A=[[-i,n] for n,i in enumerate(list(map(int,input().split(' '))))]
heapq.heapify(A)
A_max = heapq.heappop(A)
today = A_max[1]
if A_max[0]<-1:
    heapq.heappush(A,[A_max[0]+1,today])
while len(A)>1:
    a=heapq.heappop(A)
    b=heapq.heappop(A)
    if today!=a[1]:
        today = a[1]
        a[0] += 1
    else:
        today = b[1]
        b[0] += 1
    if a[0]<0:
        heapq.heappush(A,a)
    if b[0]<0:
        heapq.heappush(A,b)
if today != A[0][1]:
    print(-A[0][0]-1)
else:
    print(-A[0][0])
