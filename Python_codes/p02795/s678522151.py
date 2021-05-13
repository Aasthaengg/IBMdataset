a=int(input())
b=int(input())
c=max(a,b)
n=int(input())

if n%c==0:
  print(n//c)
else:
  print(n//c +1)