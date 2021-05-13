s = input()
if "R" not in s:
  print(0)
elif s[1] == "S":
  print(1)
elif s[0] == s[2] == "R":
  print(3)
elif s[0] == "R" or s[2] == "R":
  print(2)
else:
  print(1)