a,b,c = map(int,input().split())
A = a+b
B = a+c
C = b+c
if A <= B and A <= C:
  print(A)
elif B <= A and B <= C:
  print(B)
else:
  print(C)