import heapq

N,M= map(int,input().split())
A = list(map(lambda x: int(x)*-1,input().split()))
heapq.heapify(A)
while M:
    tmp=heapq.heappop(A)*-1
    heapq.heappush(A,tmp//2*-1)
    M -=1
print(sum(A)*-1)
    
