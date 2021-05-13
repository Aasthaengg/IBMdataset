x,y = input().split()
if x == "A":
  if y == "A":
    print("=")
  else:
    print("<")
elif x == "B":
  if y == "A":
    print(">")
  elif y == "B":
    print("=")
  else:
    print("<")
elif x == "C":
  if y == "A" or y == "B":
    print(">")
  elif y == "C":
    print("=")
  else:
    print("<")
elif x == "D":
  if y == "E" or y == "F":
    print("<")
  elif y == "D":
    print("=")
  else:
    print(">")
elif x == "E":
  if y == "F":
    print("<")
  elif y == "E":
    print("=")
  else:
    print(">")
else:
  if y == "F":
    print("=")
  else:
    print(">")