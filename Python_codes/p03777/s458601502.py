input1 = input().split()
a = input1[0]
b = input1[1]
if a == "H":
  if b == "H":
    print("H")
  else:
    print("D")
else:
  if b == "H":
    print("D")
  else:
    print("H")