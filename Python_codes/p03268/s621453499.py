n,k=map(int,input().split())
if k%2==0:
  ans=(n//k)**3+(n//(k//2)-n//k)**3
  print(ans)
else:
  print((n//k)**3)