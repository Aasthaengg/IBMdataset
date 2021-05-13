import sys
A, B, K = (int(x) for x in input().split())
if A>=K:
  A-=K
else:
  K-=A
  A=0
  if B>=K:
    B-=K
  else:
    B=0
print(A, end=" ")
print(B)