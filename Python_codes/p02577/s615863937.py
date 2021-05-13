N = str(input())

dsum = 0
for i in range(len(N)):
  dsum += int(N[i])
if dsum%9 == 0:
  print("Yes")
else:
  print("No")