import sys

s = input()
for i in range(len(s)):
  if i % 2 == 1:
    if s[i] == "R":
      print("No")
      sys.exit()
  else:
    if s[i] == "L":
      print("No")
      sys.exit()
print("Yes")
