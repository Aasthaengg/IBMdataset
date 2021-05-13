s = input()
i = s.find("C")
if i < 0:
  print("No")
  exit()
j = s.find("F", i)
if j < 0:
  print("No")
  exit()
print("Yes")
