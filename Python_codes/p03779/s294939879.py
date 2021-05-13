import math
x = int(input())
abs_x = abs(x)

num = 0
i = 1
while abs_x > num:
  num += i
  i += 1
print(i - 1)