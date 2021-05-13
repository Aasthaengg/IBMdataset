N,M=list(map(int,input().split()))
S=[[0,0]]*N
for i in range(N):
  S[i]=list(map(int,input().split()))
C=[[0,0]]*M
for j in range(M):
  C[j]=list(map(int,input().split()))

INF=float('inf')
ans=[[0,INF]]*N
for i in range(N):
  for j in range(M):
    x=abs(S[i][0]-C[j][0])
    y=abs(S[i][1]-C[j][1])
    if x+y<ans[i][1]:
      ans[i]=[j+1,x+y]
for i in range(N):
  print(ans[i][0])