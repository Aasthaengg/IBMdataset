A,B,C =map(int,input().split())
con = 0
if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
  print(0)
  exit()
if A == B and B == C:
  print(-1)
  exit()
while True:
  if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
    break
  con += 1
  D = A / 2
  E = B / 2
  F = C / 2
  A = E + F
  B = D + F
  C = D + E
  
print(con)