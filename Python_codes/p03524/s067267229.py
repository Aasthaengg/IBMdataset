S=input()
A=S.count('a')
B=S.count('b')
C=S.count('c')
if abs(A-B)<=1 and abs(C-B)<=1 and abs(A-C)<=1:
  print('YES')
else:
  print('NO')