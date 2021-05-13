n=int(input())
a=list(map(int,input().split()))
a.sort()
mod=10**9+7
if n%2==0:
  for i in range(n):
    if a[i]!=(i//2)*2+1:
      print(0)
      exit()
  print(pow(2,n//2,mod))
else:
  for i in range(n):
    if a[i]!=((i+1)//2)*2:
      print(0)
      exit()
  print(pow(2,n//2,mod))

