n=int(input())
ans=0
for i in range(1,n+1):
  k=len(str(i))
  if k%2==1:
    ans+=1
print(ans)