N,M,Q=map(int,input().split())
list=[[0 for i in range(N+1)]for j in range(N+1)]
for _ in range(M):
  L,R=map(int,input().split())
  list[L][R]+=1
for i in range(N):
  for j in range(N):
    list[i+1][j+1]+=(list[i+1][j]+list[i][j+1]-list[i][j])
for _ in range(Q):
  p,q=map(int,input().split())
  ans=list[q][q]-list[p-1][q]-list[q][p-1]+list[p-1][p-1]
  print(ans)