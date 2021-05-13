A,B,C = (x for x in input().split())

list_A = list(A)
list_B = list(B)
list_C = list(C)

if list_A[len(list_A)-1] == list_B[0] and list_B[len(list_B)-1] == list_C[0]:
  print('YES')
else:
  print('NO')