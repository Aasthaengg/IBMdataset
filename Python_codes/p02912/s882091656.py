N,M = map(int,input().split())
A = list(map(int,input().split()))
import heapq
B = []
for a in A:
    B.append(-a)
heapq.heapify(B)
for i in range(M):
    a = heapq.heappop(B)
    a = (-a)//2
    a = -a
    heapq.heappush(B,a)
print(-sum(B))