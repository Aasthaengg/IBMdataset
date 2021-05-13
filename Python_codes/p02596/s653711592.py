x=7
ans=1
k=int(input())
if k%2==0 or k%5==0:
  print(-1)
else:
  for i in range(1,k):
    if x%k==0:
      break
    x=(x*10+7)%k
    ans+=1
  print(ans)