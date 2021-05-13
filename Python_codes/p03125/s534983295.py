a,b=map(int,input().split())

if a%b==0 or b%a==0:
  print(a+b)
else:
  print(b-a)