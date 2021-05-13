import heapq
N = int(input())
A = sorted(list(map(int,input().split())))
heap = []
for i in range(N):
    a = A[i]
    heapq.heappush(heap,(a,1))
while len(heap)>1:
    a,n1 = heapq.heappop(heap)
    b,n2 = heapq.heappop(heap)
    if b<=2*a:
        a += b
        heapq.heappush(heap,(a,n1+n2))
    else:
        a += b
        heapq.heappush(heap,(a,n2))
a,n = heapq.heappop(heap)
print(n)