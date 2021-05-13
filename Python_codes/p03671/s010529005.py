A,B,C=map(int,input().split())
if A<B:
  if B<C: print(A+B)
  else: print(A+C)
else:
  if A<C: print(A+B)
  else: print(B+C)
