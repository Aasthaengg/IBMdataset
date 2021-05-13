import math
a, b = map(int, input().split())
row_a = max(1, math.ceil((a - 1) / 50) * 2)
row_b = max(1, math.ceil((b - 1) / 50) * 2)

print("{} {}".format((row_a + row_b), 100))

rest = a - 1
for i in range(row_a):
  temp = ""
  if i % 2 == 0:
    for j in range(50):
      if rest != 0:
        temp += "#."
        rest -= 1
      else:
        temp += "##"
  else:
    for j in range(50):
      temp += "##"
  print(temp)
rest = b - 1
for i in range(row_b):
  temp = ""
  if i % 2 != 0:
    for j in range(50):
      if rest != 0:
        temp += ".#"
        rest -= 1
      else:
        temp += ".."
  else:
    for j in range(50):
      temp += ".."
  print(temp)
