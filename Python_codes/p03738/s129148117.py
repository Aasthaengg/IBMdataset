from sys import exit
A = input()
B = input()
if len(A) > len(B):
  print("GREATER")
elif len(A) < len(B):
  print("LESS")
else:
  for a,b in zip(A,B):
    if a > b:
      print("GREATER")
      exit()
    elif a < b:
      print("LESS")
      exit()
  print("EQUAL")