s = input()
t = input()
if len(s) < len(t):
  print("LESS")
elif len(s) > len(t):
  print("GREATER")
else:
  for i in range(len(s)):
    if int(s[i]) < int(t[i]):
      print("LESS")
      break
    elif int(s[i]) > int(t[i]):
      print("GREATER")
      break
  else:
    print("EQUAL")