N,K=map(int,input().split())
ans=0

if K%2!=0:
  p=N//K
  ans+= p**3
else:
  z=K//2
  a=(N-z)//K+1
  ans += a**3
  p=N//K
  ans+= p**3

print(ans)
