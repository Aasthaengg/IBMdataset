s = input()
flag = False
for i in s:
  if i == "C":
    flag = True
  elif i == "F":
    if flag == True:
      print("Yes")
      break
else:
  print("No")