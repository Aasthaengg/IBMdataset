n = input()
lis = ["+", "-"]

for x in lis:
  for y in lis:
    for z in lis:
      p = n[0] + x + n[1] + y + n[2] + z + n[3]
      if eval(p) == 7:
        print(p + "=7")
        exit()
