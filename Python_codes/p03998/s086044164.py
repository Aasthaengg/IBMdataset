A,B,C = open(0).read().split()
P = "a"

for x in range(len(A)+len(B)+len(C)):
  if P=="a":
    if A=="":
      print("A")
      exit()
    else:
      P = A[0]
      A = A[1:]
      
  elif P=="b":
    if B=="":
      print("B")
      exit()
    else:
      P = B[0]
      B = B[1:]
      
  else:
    if C=="":
      print("C")
      exit()
    else:
      P = C[0]
      C = C[1:]