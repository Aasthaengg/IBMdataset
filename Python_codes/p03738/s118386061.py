a = input()
b = input()
if len(a) > len(b):
  print("GREATER")
elif len(b) > len(a):
  print("LESS")
else: #桁数が同じ
  if a == b:
    print("EQUAL")
  else:
    for i, j in zip(a, b):
      if i > j:
        print("GREATER")
        break
      elif j > i:
        print("LESS")
        break
  
  

