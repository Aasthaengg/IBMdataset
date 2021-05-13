m,k=map(int,input().split())
if k>=2**m:
  print(-1)
  exit()
if m==1 and k==1:
  print(-1)
  exit()
if k==0:
  ans=[]
  for i in range(2**m):
    ans.append(i)
    ans.append(i)
else:
  ans=[k]
  for i in range(2**m):
    if i==k:continue
    ans.append(i)
  ans.append(k)
  for i in range(2**m-1,-1,-1):
    if i==k:continue
    ans.append(i)
print(*ans,sep=' ')