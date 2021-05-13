n=int(input())

ans=0

if n%2==0:
  st=10
  d=1
  while st<=n:
    ans+=(n//st)
    st*=5
  print(ans)
else:
  print(ans)