a,b=(int(x) for x in input().split())

if b % a ==0:
  print(a+b)
elif b % a !=0:
  print(b-a)