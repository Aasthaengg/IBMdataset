n=int(input())
m=n//100
l=n%100
if l<=5*m:
  print("1")
else:
  print("0")