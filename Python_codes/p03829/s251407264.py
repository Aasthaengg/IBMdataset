n,a,b=map(int,input().split())
x=list(map(int,input().split()))
s=b//a
ans=0
for i in range(n-1):
  t=x[i+1]-x[i]
  if s<t:
    ans+=b
  else:
    ans+=a*t
print(ans)