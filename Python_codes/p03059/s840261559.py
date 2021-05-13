a,b,t=map(int,input().split())
ans=0
while t+0.5-a>0:
  ans+=b
  t-=a
print(ans)