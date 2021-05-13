n,m=input().split()
n=int(n)
m=int(m)
ans=0

if 2*n > m:
  ans+=m//2
  print(ans)
else:
  ans+=n
  m-=2*n
  ans+=m//4
  print(ans)