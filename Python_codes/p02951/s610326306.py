a, b, c = [int(i) for i in input("").split(" ")]
c-= a-b
if c > 0:
  print(c)
else:
  print(0)