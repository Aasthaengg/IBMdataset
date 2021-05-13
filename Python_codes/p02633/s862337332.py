x = int(input())
y = 360
while y % x != 0:
  y += 360
print(y // x)