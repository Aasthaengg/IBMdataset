n=int(input())
a=2
b=1
if n==1:
  print(1)
else:
  for i in range(n-1):
    if i%2==0:
      a=a+b
    else:
      b=a+b
  print(max(a,b))
