import heapq

n=int(input())
A=list(map(int,input().split()))
for i in range(n):
  A[i]*=-1
A.sort()
ans=0
Q=[A[0]]
heapq.heapify(Q)
for i in range(1,n):
  v=heapq.heappop(Q)
  v*=-1
  ans+=v
  heapq.heappush(Q,A[i])
  heapq.heappush(Q,A[i])

print(ans)