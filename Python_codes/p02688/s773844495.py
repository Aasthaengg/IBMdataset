N,M=list(map(int,input().split()))
si=[0]*N
ans=0
for i in range(M):
    S=int(input())
    who=list(map(int,input().split()))
    for k in range(S):
        si[who[k]-1]+=1
for h in range(N):
  if si[h]==0:
    ans+=1
print(ans)
