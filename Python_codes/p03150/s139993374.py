s = input()
if len(s) < 7:
  print("NO")
else:
  if s[:7] == "keyence" or s[-7:] == "keyence":
    print("YES")
  else:
    flag = True
    for i in range(1, 7):
      if s[:i]+s[i-7:] == "keyence":
        flag = False
        print("YES")
        break
    if flag:
      print("NO")