n=int(input())
if n%2==0:
  print((n*(n-1)//2-n//2))
  for i in range(1,n):
    for j in range(i+1,n+1):
      if i+j!=n+1:
        print(i,j)
else:
  print((n*(n-1)//2-(n-1)//2))
  for i in range(1,n):
    for j in range(i+1,n+1):
      if j==n:
        print(i,j)
      elif j+i!=n:
        print(i,j)