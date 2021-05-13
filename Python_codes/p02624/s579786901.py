n=int(input())
fn=[1]*(n+1)
for i in range(2,n+1):
  j=1
  while i*j<=n:
    fn[i*j]+=1
    j+=1
ans=0
for i in range(n+1):
  ans+=i*fn[i]
print(ans)