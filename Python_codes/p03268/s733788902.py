n,m = map(int,input().split())
if m % 2 == 1:
  print((n//m)**3)
else:
  print((n//m)**3 + +((n+m//2)//m)**3)
