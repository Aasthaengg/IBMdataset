A, B, C = map(str, input().split())
a = list(A)
b = list(B)
c = list(C)
 
if a[-1] == b[0] and b[-1] == c[0]:
  print('YES')
else:
  print('NO')