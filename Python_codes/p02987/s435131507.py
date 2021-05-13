s = list(input())
if len(set(s)) == 2:
  for i in set(s):
    if s.count(i) != 2:
      break
    else:
      print("Yes")
      exit()
print("No")
