A,B,C=map(str,input().split())

a=len(A)
b=len(B)

if A[a-1]==B[0] and B[b-1]==C[0]:
  print('YES')
else:
  print('NO')