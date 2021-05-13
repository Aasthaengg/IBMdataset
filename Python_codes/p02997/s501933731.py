n,k=map(int,input().split())
if k>((n-1)*(n-2))//2:
  print(-1)
  
else:
  i=0
  k=(n*(n-1))//2-k
  print(k)
  x=1
  y=2
  for i in range(k):
    print(x,y)
    if y==n:
      x+=1
      y=x+1
    else:
      y+=1