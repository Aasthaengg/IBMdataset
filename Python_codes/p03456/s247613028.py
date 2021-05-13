a,b=input().split()
c=int(a+b)
d=c**0.5
if float.is_integer(d):
  print('Yes')
else:
  print('No')