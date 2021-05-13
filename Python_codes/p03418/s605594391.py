n,k=map(int,input().split())
ans=0
if k==0:
  print(n*n)
else:
  for i in range(k+1,n+1):
    a=n//i
    b=n%i
    c=0
    if b>=k:
      c=b-k+1
    ans=ans+(i-k)*a+c
  print(ans)