import heapq
X,Y,Z,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
Q=[[-A[0]-B[0]-C[0],0,0,0]]
heapq.heapify(Q)
ans=[]
ijk={(0,0,0)}
while len(ans)<K:
  abc,i,j,k=heapq.heappop(Q)
  if i+1<X and  not (i+1,j,k) in ijk:
    ijk.add((i+1,j,k))
    heapq.heappush(Q,[-A[i+1]-B[j]-C[k],i+1,j,k])
  if j+1<Y and  not (i,j+1,k) in ijk:
    ijk.add((i,j+1,k))
    heapq.heappush(Q,[-A[i]-B[j+1]-C[k],i,j+1,k])
  if k+1<Z and  not (i,j,k+1) in ijk:
    ijk.add((i,j,k+1))
    heapq.heappush(Q,[-A[i]-B[j]-C[k+1],i,j,k+1])
  ans.append(-abc)
for i in ans:
  print(i)