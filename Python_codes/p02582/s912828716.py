w = input()

if w.count("R") == 3:
  print(3)
elif w.count("R") == 2:
  if w[1] == "S":
    print(1)
  else:
    print(2)
elif w.count("R") == 1:
  print(1)
else:
  print(0)