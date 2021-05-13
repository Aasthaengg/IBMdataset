import heapq

n,m=map(int,input().split())
a=list(map(lambda x: int(x)*(-1),input().split()))
heapq.heapify(a)

for i in range(m):
    tmp_min=heapq.heappop(a)
    if tmp_min%2==0:
        push=tmp_min/2
    else:
        push=tmp_min//2+1
    heapq.heappush(a,push)
print(int(-sum(a)))