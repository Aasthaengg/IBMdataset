n,m=map(int,input().split())
if n>=3 and m>=3:
  print((n-2)*(m-2))
elif n==1 and m>=3:
  print(m-2)
elif m==1 and n>=3:
  print(n-2)
elif n==1 and m==1:
  print(1)
else:
  print(0)