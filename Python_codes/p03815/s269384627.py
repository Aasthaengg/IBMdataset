x=int(input())
kai=x//11
amari=x%11

if 1<=amari<=6:
  print(2*kai+1)
elif 7<=amari<=10:
  print(2*kai+2)
else:
  print(2*kai)