N,M=map(int,input().split())
S=[list(map(int,input().split())) for _ in range(M)]
P=list(map(int,input().split()))

ans=0
for i in range(1<<N):
  sw=[False]*M
  for j in range(M):
    cnt=0
    for k in range(1,len(S[j])):
      if (i>>(S[j][k]-1))&1:
        cnt+=1
      else:
        flag=0
    if cnt%2==P[j]:
      sw[j]=True
  if all(sw):
    ans+=1
print(ans)