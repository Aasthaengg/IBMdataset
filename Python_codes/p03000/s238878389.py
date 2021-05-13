N,X=map(int,input().split())
L=list(map(int,input().split()))
ans=0
d=0
if d<=X:
  ans+=1
for x in range(N):
  d=d+L[x]
  if d<=X:
    ans+=1
print(ans)