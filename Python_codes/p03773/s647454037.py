A, B = map(int,input().split())
C = A + B
if C >= 24:
  C = C - 24
print(C)