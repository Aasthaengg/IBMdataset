n=int(input())
b=False
for i in range(n):
  num=int(input())
  if num%2==1:
    b=True
if b:
  print("first")
else:
  print("second")