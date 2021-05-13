a,b,c=map(int,input().split())
if a**2+b**2==c**2:
  print(a*b//2)
elif a**2+c**2==b**2:
  print(a*c//2)
else:
  print(b*c//2)