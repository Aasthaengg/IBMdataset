s = input()
t = set(s)
if len(t) == 2 and s.count(list(t)[0]) == 2:
  print("Yes")
else:
  print("No")