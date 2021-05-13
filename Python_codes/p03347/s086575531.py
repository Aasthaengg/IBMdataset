n=int(input())
arr=[int(input()) for _ in range(n)]
l=0
flag=True
for i in range(n):
  if arr[i]==0:
    l=1
  else:
    if arr[i]>l:
      flag=False
      break
    l+=1
  if i!=0:
    if arr[i]-arr[i-1]>=2:
      flag=False
      break
if flag==False:
  print(-1)
else:
  ans=arr[-1]
  tmp=arr[-1]
  for i in range(n-2,-1,-1):
    if arr[i]<tmp:
      tmp=arr[i]
    else:
      ans+=arr[i]
      if tmp!=arr[i]:
        tmp=arr[i]
  print(ans)