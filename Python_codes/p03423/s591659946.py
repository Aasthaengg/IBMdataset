n=int(input())
if n%3==0:
  a=int(n/3)
  print(a)
elif n%3==1:
  m=n-1
  a=int(m/3)
  print(a)
else:
  m=n-2
  a=int(m/3)
  print(a)