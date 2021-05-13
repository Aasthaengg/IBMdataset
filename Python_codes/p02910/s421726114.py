S = input()

check = True
for i, s in enumerate(S):
  if (i+1)%2 == 0:
    if not(s == "L" or s == "U" or s == "D"):
      check = False
  else:
    if not(s == "R" or s == "U" or s == "D"):
      check = False

if check:
  print("Yes")
else:
  print("No")