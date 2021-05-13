A=int(input())
B=int(input())
C=int(input())
D=int(input())

if A>=B and C>=D:
  print(B+D)
elif A<B and C>D:
  print(A+D)
elif A>B and C<D:
  print(B+C)
else:
  print(A+C)