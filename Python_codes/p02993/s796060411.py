S = input()
flag = False
for s in S:
  if flag:
    if temp == s:
      print("Bad")
      quit()
  temp = s
  flag = True
print("Good")
