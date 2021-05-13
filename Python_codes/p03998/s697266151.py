AA = input()
A =list(AA)
BB = input()
B = list(BB)
CC = input()
C = list(CC)

X ='a'

while True:
  
  if X  == 'a':
    if len(A) == 0:
        break
    else:
        X = A.pop(0)  
  elif X =='b':
    if len(B) ==0:
        break
    else:
        X = B.pop(0)
  else:
    if len(C) == 0:
        break
    else:
        X = C.pop(0)
print(X.upper())
