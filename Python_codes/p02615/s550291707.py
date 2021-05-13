import heapq

N=int(input())
A=sorted(list(map(int,input().split())), reverse=True)
ans=0
H=[-1*A[0]]
heapq.heapify(H)
for a in A[1:]:
  ans-=heapq.heappop(H)
  heapq.heappush(H,-1*a)
  heapq.heappush(H,-1*a)
print(ans)