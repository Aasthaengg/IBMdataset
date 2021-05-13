n,k=map(int,input().split())
if k>((n-1)*(n-2))//2:
  print(-1)
else:
  m=((n-1)*(n-2))//2
  d=m-k
  print(n-1+d)
  for i in range(n-1):
    print(1,i+2)
  if d==0:exit()
  for i in range(2,n):
    for j in range(i+1,n+1):
      print(i,j)
      d-=1
      if d==0:
        exit()
