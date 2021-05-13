A=int(input())
B=int(input())
C=int(input())
D = int(input())
S=0
if A >= B:
  S += B
  if C >= D:
    S += D
  else:
    S += C
else:
  S += A
  if C >= D:
    S += D
  else:
    S += C
print(S)