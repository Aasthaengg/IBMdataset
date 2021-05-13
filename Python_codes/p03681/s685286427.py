n,m=map(int,input().split())
ans=0
if n==m:
  ans=1
  for i in range(n):
    ans=(ans*(n-i)*(m-i))%(10**9+7)
  ans=(ans*2)%(10**9+7)
elif n+1==m:
  ans=m
  for i in range(n):
    ans=(ans*(n-i)*(m-i-1))%(10**9+7)
elif m+1==n:
  ans=n
  for i in range(m):
    ans=(ans*(m-i)*(n-i-1))%(10**9+7)
print(ans)