N,M=map(int,input().split())
KA=[0]*N
count=[0]*(M+1)
for i in range(N):
  KA[i]=list(map(int,input().split()))
for i in range(N):
  for j in range(1,len(KA[i])):
    count[KA[i][j]]+=1
ans=0
for i in range(1,M+1):
  if count[i]==N :
    ans+=1
print(ans)