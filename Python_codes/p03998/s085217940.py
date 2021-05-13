A = input()
B = input()
C = input()

check = A[0]
A = A[1:]
while True:
  if check == "a":
    if len(A) == 0:
      print("A")
      exit()
    check = A[0]
    A = A[1:]
  elif check == "b":
    if len(B) == 0:
      print("B")
      exit()
    check = B[0]
    B = B[1:]
  elif check == "c":
    if len(C) == 0:
      print("C")
      exit()
    check = C[0]
    C = C[1:]