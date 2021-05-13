s = input()
s_r = "".join(list(reversed(s)))
if s == s_r:
  print("Yes")
else:
  print("No")