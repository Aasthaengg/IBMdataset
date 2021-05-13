s = input()
x = list(set(s))
if len(x) == 2:
  if s.count(x[0])==2 and s.count(x[1])==2:
    print("Yes")
  else:
    print("No")
else:
  print("No")