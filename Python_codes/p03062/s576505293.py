N=int(input())
A=list(map(int,input().split()))
A.sort()
count=0
zer=0
for i in range(N):
  if A[i]<0:
    count+=1
  if A[i]==0:
    zer+=1
ans=0
if zer!=0:
  for i in range(N):
    if A[i]<0:
      A[i]=-A[i]
    ans+=A[i]
else:
  if count%2==0:
    for i in range(N):
      if A[i]<0:
        A[i]=-A[i]
      ans+=A[i]
  else:
    for i in range(N):
      A[i]=abs(A[i])
    A.sort()
    ans=sum(A[1:])-A[0]
print(ans)