A=input()
B=input()
A='0'*(101-len(A))+A
B='0'*(101-len(B))+B
if A>B:
  print('GREATER')
elif A<B:
  print('LESS')
else:
  print('EQUAL')