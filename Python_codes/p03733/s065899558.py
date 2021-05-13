n,t=map(int,input().split())
a=list(map(int,input().split()))
ans=t
for i in range(n-1):
  b=a[i+1]-a[i]
  if b>t:
    ans+=t
  else:
    ans+=b
print(ans)