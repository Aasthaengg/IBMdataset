A = input()
B = input()
C = input()

x = A[0]

def turn(A, B, C, x):
  if x == 'a':
    if len(A) == 0:
      print('A')
      return
    else:
      y = A[0]
      A = A[1:]
      
  if x == 'b':
    if len(B) == 0:
      print('B')
      return
    else:
      y = B[0]
      B = B[1:]
  
  if x == 'c':
    if len(C) == 0:
      print('C')
      return
    else:
      y = C[0]
      C = C[1:]
  
  return turn(A, B, C, y)

turn(A, B, C, x)