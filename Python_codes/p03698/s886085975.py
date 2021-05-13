s = input()
s = list(s)

s_unique = list(set(s))
if len(s) == len(s_unique):
  print("yes")
else :
  print("no")