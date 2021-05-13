n=int(input())
if n==1:
  print(1)
else:
  for i in range(9):
    a=2**i
    if  a>n:
      print(a//2)
      break