d,n=map(int,input().split())
k=100**d
if n%100==0:
  n+=n//100
ans=n*k

print(ans)