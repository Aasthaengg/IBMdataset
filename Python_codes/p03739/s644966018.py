n=int(input())
a=list(map(int,input().split()))
m=0
curr=1
ans=0
for i in range(n):
  m+=a[i]
  if curr*m<=0:
    ans+=1-curr*m
    m=curr
  curr=-1*curr
ans2=0
m=0
curr=-1
for i in range(n):
  m+=a[i]
  if curr*m<=0:
    ans2+=1-curr*m
    m=curr
  curr=-1*curr
print(min(ans,ans2))