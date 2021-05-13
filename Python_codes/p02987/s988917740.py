str = input()
a1 = str[0]
a2 = str[1]
a3 = str[2]
a4 = str[3]

if str.count(a1) == 2 and str.count(a2) == 2 and str.count(a3) == 2 and str.count(a4) == 2:
  print("Yes")
else:
  print("No")