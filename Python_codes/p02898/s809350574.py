n,k=map(int,input().split())
ls=list(map(int,input().split()))
ans=0
for item in ls:
  if item<k:
    ans+=1
print(n-ans)