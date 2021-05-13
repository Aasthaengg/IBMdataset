A=input()
B=input()
a=len(A)
b=len(B)

def less():
  print('LESS')
  exit()
def greater():
  print('GREATER')
  exit()
def equals():
  print('EQUAL')
  exit()

if a<b:
  less()
if a>b:
  greater()
for i in range(a):
  if int(A[i])<int(B[i]):
    less()
  if int(A[i])>int(B[i]):
    greater()
else:
  equals()