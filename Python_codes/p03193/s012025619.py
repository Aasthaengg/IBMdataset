ans=0
N,A,B=map(int,input().split())
for i in range(N):
  A1,B2=map(int,input().split())
  if A<=A1 and B<=B2:
    ans+=1
print(ans)