import heapq

N=int(input())
arr=list(map(int,input().split()))
hq=[]

for i in range(N):
    heapq.heappush(hq,arr[i])
    
while len(hq)>1:
    a=heapq.heappop(hq)
    b=heapq.heappop(hq)
    heapq.heappush(hq,(a+b)/2)

print(*hq)