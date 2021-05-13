n=int(input())
mod=10**9+7
a=list(map(int,input().split()))
ans=[0]*(10**5+1)
flag=False
if n%2==0:
  for i in range(len(a)):
    if a[i]%2==0:
      flag=True
      break
    ans[a[i]]+=1
    if ans[a[i]]>2:
      flag=True
      break
else:
  for i in range(len(a)):
    if a[i]%2==1:
      flag=True
      break
    ans[a[i]]+=1
    if ans[0]>1:
      flag=True
      break
    if ans[a[i]]>2:
      flag=True
      break
if flag==True:
  print(0)
else:
  print(pow(2,(n//2),mod))
