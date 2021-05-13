X=int(input())

n = X//100

if X in range(n*100,n*105+1):
  print(1)
else:
  print(0)