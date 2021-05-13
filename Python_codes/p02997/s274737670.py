[n,k]=[int(x) for x in input().split()]

x=((n-1)*(n-2))//2 - k

if x<0:
  print(-1)
else:
  print(n-1+x)
  for i in range(2,n+1):
    print(1,i)
  for i in range(2,n):
    for j in range(i+1,n+1):
      if x == 0:
        exit()
      print(i,j)
      x -= 1