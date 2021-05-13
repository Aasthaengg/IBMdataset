A,B = map(int,input().split())

if A == B:
  print(0)
  exit(0)

C = 0
# 符号が同じ
if A * B > 0:
  if A < B:
    C = abs(B - A)
  else:
    C = abs(B - A) + 2
# 符号が違う
elif A * B < 0:
  C = abs(abs(B) - abs(A)) + 1
# どちらかが0
else:
  if A == 0:
    C = abs(B)
    if B < 0:
      C += 1
  elif B == 0:
    C = abs(A)
    if 0 < A:
      C += 1
  
  
  
print(C)
    
    

