from heapq import heapify,heappush,heappop

N=int(input())
V=list(map(int,input().split()))
heapify(V)

while len(V)>=2:
    a=heappop(V)
    b=heappop(V)
    heappush(V,(a+b)/2)

c=heappop(V)
print(c)
