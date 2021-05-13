s = input()
f = 0
for i in range(len(s)):
  if f == 0 and s[i] == "C":
    f = 1
  if f == 1 and s[i] == "F":
    f = 2
    break
if f == 2:
  print("Yes")
else:
  print("No")