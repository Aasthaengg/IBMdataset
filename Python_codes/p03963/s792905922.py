n,k=map(int,input().split())
if n==1:
  print(k)
else:
  sum=k
  for i in range(n-1):
    sum*=k-1
  print(sum)