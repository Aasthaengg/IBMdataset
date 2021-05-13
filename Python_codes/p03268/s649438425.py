[n,k]=[int(x) for x in input().split()]

if k%2==1:
  print((n//k)**3)
else:
  print((n//k)**3+(n//(k//2)-(n//k))**3)