n = int(input())
bol = 0
for i in range(1,10):
  for j in range(1,10):
    if i*j == n:
      bol = 1
      break
if bol == 1:
  print("Yes")
else:
  print("No")