A,B,K=map(int,input().split())
if A>=K:
  A=A-K
else:
  B=B-(K-A)
  if B<0:
    B=0
  A=0
print(A,B)
