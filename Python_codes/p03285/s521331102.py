n=int(input())
exist=False
for i in range(n):
  for j in range(n):
    if 4*i+7*j==n:
      print("Yes")
      exist=True
    if exist:
      break
  if exist:
    break
if not exist:
  print("No")