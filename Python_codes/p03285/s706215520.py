N = int(input())
M = [4*i+7*j for i in range(100) for j in range(100)]

if N in M:
  print("Yes")
else:
  print("No")