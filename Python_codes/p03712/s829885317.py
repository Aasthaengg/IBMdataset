H, W = map(int, input().split())
for i in range(W + 2):
  print("#", end="")
print("")
for i in range(H):
  print("#", end="")
  print(input(), end="")
  print("#")
for i in range(W + 2):
  print("#", end="")
print("")