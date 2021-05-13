X=int(input())
amari=X%100
num=(X-amari)//100
num*=5
if num>=amari:
  print(1)
else:
  print(0)
