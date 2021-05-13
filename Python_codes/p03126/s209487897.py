N,M=map(int,input().split())
Like=[0 for i in range(M)]
A=[[] for i in range(N)]
for i in range(N):
  A[i]=[int(x) for x in input().split()]
for i in range(N):
  for j in range(1,A[i][0]+1):
    Like[A[i][j]-1]=Like[A[i][j]-1]+1
print(Like.count(N))