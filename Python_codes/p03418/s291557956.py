n,k=map(int,input().split())
ans=0
for b in range(k+1,n+1):
  q=n//b
  s=n%b
  ans+=q*(b-k)
  if s>=k:
    ans+=s-k+1
if k==0:
  ans-=n
print(ans)