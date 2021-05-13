s1 = list(input())
s2 = list('abcdefghijklmnopqrstuvwxyz')
r = sorted(list(set(s2) - set(s1)))
if len(r) == 0:
  print("None")
else:
  print(r[0])