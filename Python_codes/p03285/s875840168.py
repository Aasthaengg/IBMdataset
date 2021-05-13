N = int(input())
arr = []

for i in range(0,1+100//4):
  for j in range(0,1+100//7):
    if 4*i + 7*j <= 100:
      arr.append(4*i+7*j)

if N in arr:
  print("Yes")
else:
  print("No")