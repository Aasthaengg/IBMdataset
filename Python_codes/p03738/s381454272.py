import math
A = input()
B = input()
if len(A)>len(B):
  print("GREATER")
elif len(A)<len(B):
  print("LESS")
else:
  while 1:
    if int(A[0])>int(B[0]):
      print("GREATER")
      break
    elif int(A[0])<int(B[0]):
      print("LESS")
      break
    else:
      if len(A)!=1:
        A = A[1:]
        B = B[1:]
      else:
        if int(A)>int(B):
          print("GREATER")
          break
        elif int(A)<int(B):
          print("LESS")
          break
        else:
          print("EQUAL")
          break