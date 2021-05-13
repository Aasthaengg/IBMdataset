N,C,K=map(int,input().split())
import heapq
T=[]
heapq.heapify(T)
for i in range(N):
    heapq.heappush(T,int(input()))

ans=1
p=1
start=heapq.heappop(T)

for i in range(N-1):
    t=heapq.heappop(T)
    p+=1
    if p<=C and t<=start+K:
        continue
    else:
        start=t
        ans+=1
        p=1

print(ans)