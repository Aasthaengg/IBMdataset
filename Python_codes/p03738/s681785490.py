a = input()
b = input()

if(len(a) > len(b)):
  print("GREATER")
elif(len(a) < len(b)):
  print("LESS")
elif(len(a) == len(b)):
  if(int(a) == int(b)):
    print("EQUAL")
  elif(int(a) > int(b)):
    print("GREATER")
  else:
    print("LESS")