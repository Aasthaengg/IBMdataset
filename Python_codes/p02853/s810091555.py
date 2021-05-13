X, Y = map(int, input().split())

def cos(c):
  if c==1:
    return 300000
  elif c==2:
    return 200000
  elif c==3:
    return 100000
  else:
    return 0
  
print(cos(X)+cos(Y)+ ( 400000 if X==1 and Y==1 else 0))