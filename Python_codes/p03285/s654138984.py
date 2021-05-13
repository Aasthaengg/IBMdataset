n=int(input())
a=0
for i in range(26):
  for j in range(15):
    if 4*i+7*j==n:
      a=1
      break
if a==1:
  print("Yes")
else:
  print("No")