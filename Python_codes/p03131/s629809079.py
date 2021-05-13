k,a,b=map(int,input().split())
t=a
ans=k+1
k-=a-1
t+=(b-a)*(k//2)
if k%2==0:
  ans=max(ans,t)
else:
  ans=max(ans,t+1)
print(ans)