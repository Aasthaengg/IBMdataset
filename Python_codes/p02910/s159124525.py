s = input()
n = len(s)
c = 0
for i in range(n):
  if (i%2 == 0):
    if (s[i] == "L"):
      c = 1
  else:
    if (s[i] == "R"):
      c = 1
if (c == 0):
  print("Yes")
else:
  print("No")