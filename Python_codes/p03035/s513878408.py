import math
x = input().split()
a = int(x[0]) # 年齢
b = int(x[1])
if a <= 5:
  print(0)
elif a >= 6 and a <= 12:
  print(math.floor(b/2))
else:
  print(b)