x = int(input())
mul = 1
while (mul*360) % x != 0:
  mul += 1
print(mul*360//x)