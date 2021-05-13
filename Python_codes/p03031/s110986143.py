N,M=map(int,input().split())
KS=[list(map(int,input().split())) for _ in range(M)]
p=list(map(int,input().split()))
ans=0
for i in range(1<<N):
  judge=1
  for j in range(M):
    cnt=0
    for k in KS[j][1:]:
      if i>>(k-1)&1:
        cnt+=1
    if (cnt%2)!=p[j]:
      judge=0
  if judge==1:
    ans+=1
print(ans)