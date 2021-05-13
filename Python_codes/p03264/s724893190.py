n=int(input())
if n%2==0:
  print('{:.0f}'.format((n/2)**2))
else:
  print('{:.0f}'.format((n+1)/2*(n-1)/2))