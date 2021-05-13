a,b,t=map(int,input().split())
ans=0
temp=a
while temp<t+0.5:
  ans=ans+b
  temp=temp+a
print(ans)