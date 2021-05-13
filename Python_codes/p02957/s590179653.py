A,B = map(int,input().split())

temp = A+B
if temp%2!=0:
  print("IMPOSSIBLE")
else:
  print(temp//2)