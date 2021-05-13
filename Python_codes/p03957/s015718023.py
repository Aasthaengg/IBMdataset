S = input()
f = 0
for s in S:
  if f==0:
    if s=="C":
      f = 1
  elif f==1:
    if s=="F":
      f = 2
if f == 2:
  print("Yes")
else:
  print("No")