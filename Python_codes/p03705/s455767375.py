n,a,b=map(int,input().split())

if a>b:
  print(0)
elif a==b:
  print(1)
elif n==1:
  print(0)
elif n==2:
  print(2)
else:
  print((b-a)*(n-2)+1)