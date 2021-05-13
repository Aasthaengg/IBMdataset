x = int(input())

p = x // 11
r = x % 11

if (r == 0):
  print(2 * p)
elif (r > 0 and r <= 6):
  print(2 * p + 1)
else:
  print(2 * p + 2)