n=int(input())
h=list(map(int,input().split()))
flag=False
ans,cnt=0,0

for i in range(max(h)):
  flag=False
  cnt=0
  for j in range(n):
    if h[j]>0 and flag==False:
      flag=True
      cnt+=1
    if h[j]<=0 and flag==True:
      flag=False
  ans+=cnt
  for j in range(n):
    h[j]-=1
print(ans)