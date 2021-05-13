n=int(input())
if n==1:
  print(1)
  exit()
a=list(map(int,input().split()))
ans=1
if a[0]<a[1]:flag=1
elif a[0]>a[1]:flag=-1
else:flag=0
for i in range(1,n-1):
  if flag==1 and a[i]>a[i+1]:
    ans+=1
    flag=0
  elif flag==-1 and a[i]<a[i+1]:
    ans+=1
    flag=0
  else:
    if a[i]>a[i+1]:flag=-1
    elif a[i]<a[i+1]:flag=1
print(ans)