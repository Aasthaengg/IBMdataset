import heapq
 
N,M = map(int,input().split())
Price_List = list(map(lambda x:x*(-1),map(int,input().split())))
heapq.heapify(Price_List)
for i in range(M):
    val = heapq.heappop(Price_List)* -1 // 2 * -1
    heapq.heappush(Price_List,val)
print(-sum(Price_List))
