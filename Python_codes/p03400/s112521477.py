N=int(input())
D,X=map(int,input().split())
ans=X
for i in range(N):
  A=int(input())
  j=0
  while j*A+1<=D:
    ans+=1
    j+=1
print(ans)