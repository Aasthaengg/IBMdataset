a,b,c,k=map(int,input().split())
ans=0

if k<=a:
  print(k)
elif k>a:
  k-=a
  ans+=a
  if k<=b:
    print(ans)
  elif k>b:
    k-=b
    ans-=k
    print(ans)