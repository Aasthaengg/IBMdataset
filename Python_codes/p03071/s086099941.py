a,b=map(int,input().split())
if a>b and a-b>=2:
  print(2*a-1)
elif a>b and a-b<2:
  print(a+b)
elif b>a and b-a>=2:
  print(2*b-1)
elif b>a and b-a<2:
  print(a+b)
elif a==b:
  print(a+b)