n,k=map(int,input().split())
if k%2:
  print((n//k)**3)
else:
  l=k//2
  print(((n+l)//k)**3+(n//k)**3)