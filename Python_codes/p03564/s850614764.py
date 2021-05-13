n=int(input())
k=int(input())
ans=1
for i in range(1,n+1):
  if ans*2>ans+k:
    ans+=k
  else:
    ans*=2
print(ans)
