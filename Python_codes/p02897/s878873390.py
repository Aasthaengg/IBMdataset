n = int(input())

if n % 2 == 0:
  print("{:.9f}".format(0.5))

else:
  print("{:.9f}".format((n + 1) // 2 / n))
