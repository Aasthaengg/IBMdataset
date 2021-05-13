from heapq import heapify, heappop, heappush
 
N, M = map(int, input().split())
A = [-1*int(i) for i in input().split()]

heapify(A)

for i in range(M):
    n = -1 * heappop(A)
    heappush(A, -1*(n//2))
    #print(n, A)
 
print(-1*sum(A))