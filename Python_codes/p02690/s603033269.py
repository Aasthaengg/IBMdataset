X = int(input())
for a in range(120):
  for b in range(120):
    if a**5-b**5 == X:
      print(a, b)
      exit()
    elif a**5+b**5 == X:
      print(a, -b)
      exit()

