n,k=map(int,input().split())
a=list(map(int,input().split()))
ans,l=0,0
for i in range(40)[::-1]:
  b=1<<i
  c=sum(bool(x&b) for x in a)
  if l+b<=k and c<n-c:
    l+=b
    ans+=b*(n-c)
  else:
    ans+=b*c
print(ans)