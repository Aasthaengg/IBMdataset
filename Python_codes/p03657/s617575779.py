A, B = input().split(" ")

A = int(A)
B = int(B)
C = A + B

if A % 3 == 0 or B % 3 == 0 or C % 3 == 0:
  print("Possible")
else:
  print("Impossible")