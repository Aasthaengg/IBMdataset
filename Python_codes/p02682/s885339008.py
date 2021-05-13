a,b,c,k=list(map(int,input().split()))
if k<=a+b:
  print(min(a,k))
else:
  print(2*a-k+b)