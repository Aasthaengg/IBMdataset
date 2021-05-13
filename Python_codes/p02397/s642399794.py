for x, y in ((int(i) for i in j.split()) for j in iter(input, "0 0")):
  print(y, x) if x > y else print(x, y)