import heapq
NM,a=open(0).read().rstrip().split('\n')
N,M=map(int,NM.split())
A=list(map(int,a.split()))
A=[-1*i for i in A]
heapq.heapify(A)
for i in range(M):
    sample=heapq.heappop(A)
    sample=-1*sample//2
    heapq.heappush(A,-1*sample)
print(-sum(A))