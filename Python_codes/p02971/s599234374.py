n=int(input())

import heapq
a=[]
a_heap=[]
for i in range(n):
    tmp=int(input())
    a.append(tmp)
    heapq.heappush(a_heap,(-1)*tmp)

for i in range(n):
    max_1=heapq.heappop(a_heap)
    if max_1==(-1)*a[i]:
        max_2=heapq.heappop(a_heap)
        print((-1)*max_2)
        heapq.heappush(a_heap,max_2)
    else:print((-1)*max_1)
    heapq.heappush(a_heap,max_1)