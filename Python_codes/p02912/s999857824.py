import heapq
N,M=map(int,input().split())
A=list(map(lambda x:-int(x),input().split()))
heapq.heapify(A)

for _ in range(M):
    a=-heapq.heappop(A)
    a//=2
    heapq.heappush(A,-a)

print(-sum(A))