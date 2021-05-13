n=int(input())
p=list(map(int,input().split()))

judge=[False]*n

for i in range(n):
  if p[i]==i+1:
    judge[i]=True

ans=0

for i in range(n):
  if judge[i]==True:
    ans+=1
    if i!=n-1:
      judge[i+1]=False
      
print(ans)