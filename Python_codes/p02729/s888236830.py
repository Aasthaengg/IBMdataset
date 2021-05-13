n,m=map(int,input().split())

if n<2 and m<2:
  print(0)
else:
  print(int(n*(n-1)/(2)+m*(m-1)/2))