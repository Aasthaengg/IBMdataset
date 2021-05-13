N,A,B=map(int,input().split())
a=list(map(int,input().split()))
border=B//A+1
ans=0
for i in range(N-1):
  d=a[i+1]-a[i]
  if d>=border:
    ans+=B
  else:
    ans+=(A*d)
print(ans)