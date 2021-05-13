A, B, C, D = input().split()
 
AC = int(A)*int(C)
AD = int(A)*int(D)
BC = int(B)*int(C)
BD = int(B)*int(D)

 
l = [AC, AD, BC, BD]

print(max(l))