a,b,c=map(int,input().split())
if b>=c:
  print(b+c)
else:
  ans=2*b
  c-=b
  if a>=c:
    ans+=c
  else:
    ans+=a+1
  print(ans)
