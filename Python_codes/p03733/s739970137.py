n,t=map(int,input().split())
lt=list(map(int,input().split()))

dif=[lt[i+1]-lt[i] for i in range(n-1)]

ans=0
for i in dif:
  if i <= t:
    ans+=i
  else:
    ans+=t
  
print(ans+t)