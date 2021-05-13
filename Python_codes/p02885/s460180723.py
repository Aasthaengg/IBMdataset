a, b = [int(i) for i in input("").split(" ")]
if a < 2*b:
  print(0)
else:
  print(a - 2*b)