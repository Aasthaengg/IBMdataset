A=input()
B=input()
C=input()

l='a'

for i in range(300):
  if l=='a':
    if len(A)==0:
      print('A')
      exit()
    elif len(A)==1:
      l=A[0]
      A=''
    else:
      l=A[0]
      A=A[1:]
  elif l=='b':
    if len(B)==0:
      print('B')
      exit()
    elif len(B)==1:
      l=B[0]
      B=''
    else:
      l=B[0]
      B=B[1:]
  else:
    if len(C)==0:
      print('C')
      exit()
    elif len(C)==1:
      l=C[0]
      C=''
    else:
      l=C[0]
      C=C[1:]    

