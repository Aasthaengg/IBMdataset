n,m=[int(x) for x in input().rstrip().split()]
ans=0
if n*2>m:
  print(m//2)
else:
  ans+=n
  m-=n*2
  ans+=m//4
  print(ans)