n,k=map(int,input().split())
a=list(map(int,input().split()))
ans1=[]
ans2=[]
ans1+=a
ans2+=a
for i in range(min(k,50)):
  now=0
  ans2=[]
  ans2+=ans1
  kans=[0]*n
  for j in range(n):
    if j+ans2[j]+1<=n-1:
      kans[j+ans2[j]+1]-=1
    now+=1+kans[j]
    #基本kans[j]は0だが終点は-1
    ans1[j]=now
  if ans1==list(range(1,n+1)):
    ans1=[n]*n
    break
  now=0
  kans=[0]*n
  for j in range(1,n+1):
    if n-j-ans2[n-j]>=0:
      kans[n-j-ans2[n-j]-1]-=1
    now+=1+kans[n-j]
    #基本kans[j]は0だが終点は-1
    ans1[n-j]+=now-1



print(*ans1) 
