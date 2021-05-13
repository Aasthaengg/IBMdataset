N,M = list(map(int,input().split()))
A = list(map(int,input().split()))
for i in range(N):
    A[i] = A[i]*(-1)
import heapq
heapq.heapify(A)
for i in range(M):
    X = heapq.heappop(A)
    X = (-1*X)//2
    heapq.heappush(A, -1*X)

print(sum(A)*(-1))
