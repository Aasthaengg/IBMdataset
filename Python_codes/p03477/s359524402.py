A,B,C,D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if (A+B) > (C+D):
  print ("Left")
elif (A+B) == (C+D):
  print ("Balanced")
else:
  print ("Right")