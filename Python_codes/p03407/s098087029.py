import sys

a, b, c = list(map(int, input().split()))

for i in range(2):
  for j in range(2):
    if a * i + b * j >= c:
      print("Yes")
      sys.exit()

print("No")

