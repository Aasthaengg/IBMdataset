A,B,C = map(int,input().split())
ans = 0
Aj = 0
Bj = 0
Cj = 0
if(A % 2 == 1):
  Aj = 1
if(B % 2 == 1):
  Bj = 1
if(C % 2 == 1):
  Cj = 1
if(Aj == Bj and Bj == Cj):
  pass
else:
  if(Aj == Bj):
    A += 1
    B += 1
    ans += 1
  if(Bj == Cj):
    B += 1
    C += 1
    ans += 1
  if(Aj == Cj):
    A += 1
    C += 1
    ans += 1
mokuhyo = max(A,B,C)
while(A != mokuhyo):
  A += 2
  ans += 1
while(B != mokuhyo):
  B += 2
  ans += 1
while(C != mokuhyo):
  C += 2
  ans += 1
print(str(ans))