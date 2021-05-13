def hantei(x,y):
  for Z in range(-100,100+1):
    flag=True
    for i in x:
      if i>=Z:
        flag=False
        break
    for i in y:
      if i<Z:
        flag=False
        break
    if flag==True:
      return False
  return True

N,M,X,Y=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
x.append(X)
y.append(Y)
print("War" if hantei(x,y)==True else "No War")
