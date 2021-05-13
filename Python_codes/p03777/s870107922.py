A, B = list(map(str, input().split())) 

if A == "H":
  if B == "H":
    print("H")
  else:
    print("D")

elif A == "D":
  if B == "H":
    print("D")
  else:
    print("H")