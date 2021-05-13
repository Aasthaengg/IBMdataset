A, B, C = map(int, input().split())

i = 0
Ap = A
Bp = B
Cp = C
while A%2 == 0 and B%2 == 0 and C%2 == 0:
  A = Bp//2 + Cp//2 
  B = Ap//2 + Cp//2 
  C = Bp//2 + Ap//2 
  i += 1
  Ap = A
  Bp = B
  Cp = C
  if A == B == C:
    i = -1
    break


print(i)