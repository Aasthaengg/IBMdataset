s=input()
x,y=map(int, input().split())
X,Y=[],[]
t,c=0,0
for i in range(len(s)):
  if s[i]=='F':
    c+=1
  else:
    if t%2==0:
      X.append(c)
    else:
      Y.append(c)
    c=0
    t+=1
if t%2==0:
  X.append(c)
else:
  Y.append(c)
if len(X)>0:
  D=[X[0]]
  E=[]
  for i in range(1,len(X)):
    for j in D:
      E.append(j+X[i])
      E.append(j-X[i])
    D,E=list(set(E)),[]
if x not in D:
  print('No')
  exit()
  
if len(X)>0:
  D=[0]
  E=[]
  for i in range(len(Y)):
    for j in D:
      E.append(j+Y[i])
      E.append(j-Y[i])
    D,E=list(set(E)),[]
if y not in D:
  print('No')
else:
  print('Yes')