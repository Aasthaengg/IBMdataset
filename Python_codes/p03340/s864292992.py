n=int(input())
a=list(map(int,input().split()))
a+=[None]
ans=0
if n==1:print(1);exit()
r=0
check=a[0]
for i in range(n):
  if r==n-1:
    ans+=(r-i+1)*(r-i+2)//2
    break
  for j in range(r+1,n+1):
    if j==n:
      ans+=j-i
      r=j-1
      break
    if check^a[j]==check+a[j]:
      check+=a[j]
    else:
      ans+=j-i
      r=j-1
      break
  check^=a[i]
print(ans)