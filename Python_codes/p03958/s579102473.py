import numpy as np
k,t=map(int,input().split())
a=list(map(lambda x:-int(x),input().split()))
a.sort()
import heapq
heapq.heapify(a)
b=heapq.heappop(a)
b+=1
while len(a)>0:
    c=heapq.heappop(a)
    if b<0:
        heapq.heappush(a,b)
    b=c+1
print(-b)