S = input()

rlt = 0
b = ''
tA = 0
A = 0
BC = 0
for s in S:
  if s == 'A':
    if b == 'A':
      tA += 1
    elif b == 'B':
      rlt += A*BC
      tA = 1
      A = 0
      BC = 0
    else:
      rlt += A*BC
      tA = A + 1
      A = 0
      BC = 0
  elif s == 'B':
    if b == 'B':
      rlt += A*BC
      tA = 0
      A = 0
      BC = 0
  elif s == 'C':
    if b == 'B':
      A += tA
      tA = 0
      BC += 1
    else:
      rlt += A*BC
      tA = 0
      A = 0
      BC = 0
  b = s

rlt += A*BC
  
print(rlt)