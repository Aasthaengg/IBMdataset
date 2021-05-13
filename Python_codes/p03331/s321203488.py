n=int(input())
if n in [10,100,1000,10000,100000]:
  print(10)
else:
  x=str(n)
  ans=0
  for i in x:
    ans+=int(i)
  print(ans)