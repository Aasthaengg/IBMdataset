A = input().split(" ")
L = int(A[0])+int(A[1])
R = int(A[2])+int(A[3])
if L>R:
  print("Left")
elif L == R:
  print("Balanced")
else :
  print("Right")