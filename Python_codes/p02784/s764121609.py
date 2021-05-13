H, _ = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

if sum(A) < H:
  print("No")
else:
  print("Yes")