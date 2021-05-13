from heapq import heappop, heappush, heapify

N, M = map(int,input().split())
A = list(map(int, input().split()))
A = list(map(lambda x: x*(-1), A))
heapify(A)

for i in range(M):
    temp = int(heappop(A)/2)
    heappush(A, temp)

print(-sum(A))