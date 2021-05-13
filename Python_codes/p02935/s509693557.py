from heapq import heappop,heappush,heapify

N = int(input())
heap = list(map(int,input().split()))
heapify(heap)

while(len(heap)>=2):
    x = heappop(heap)
    y = heappop(heap)
    #print(x,y)
    heappush(heap,(x+y)/2)
print(heappop(heap))