ABCD = input()
A = int(ABCD[0])
B = int(ABCD[1])
C = int(ABCD[2])
D = int(ABCD[3])
if (A==B and B==C and C==D and D==A) or (A==B and B==C and C==A) or (B==C and C==D and D==B) :
  print("Yes")
else:
  print("No")