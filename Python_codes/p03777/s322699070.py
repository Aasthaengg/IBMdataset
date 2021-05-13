a, b = map(str, input().split())
count = 0
if a == "D" and b == "H":
  count += 1
elif a == "H" and b == "D":
  count += 1
if count == 1:
  print("D")
else:
  print("H")